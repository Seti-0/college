#! /bin/bash

function evaluate {
    case "$3" in
        "^") result=$(($1 ** $2));;
        "*") result=$(($1 * $2));;
        "/") result=$(($1 / $2));;
        "+") result=$(($1 + $2));;
        "-") result=$(($1 - $2));;
    esac
}

function check_output_length {

    local count=0
    local i
    for ((i=1;i<${#tokens[@]}-1;i+=2)) do

        # Yes, shellcheck, we do actually want pattern matching on the RHS
        # shellcheck disable=SC2053
        if [[ ${tokens[$i]} != $level_pattern ]]; then
            ((count++))
        fi

    done

    result=$((2*count+1))

}

function evaluate_level {

    local new_tokens

    if [[ "$level_order" = ltr ]]; then

        local i=0 j=0

        local N=${#tokens[@]}
        while [[ i+2 -lt $N ]]; do

            # shellcheck disable=SC2053
            if [[ ${tokens[i+1]} == $level_pattern ]]; then

                local a=${tokens[i]}
                local op=${tokens[i+1]}
                local b=${tokens[i+2]}

                evaluate "$a" "$b" "$op"
                tokens[i+2]=$result
            
            else

                new_tokens[j]=${tokens[i]}
                new_tokens[j+1]=${tokens[i+1]}
                ((j+=2))
            
            fi

            ((i+=2))

        done

    elif [[ "$level_order" = rtl ]]; then

        local i=$((${#tokens[@]}-1))

        check_output_length
        local j=$((result-1))

        while [[ i-2 -ge 0 ]]; do

            # shellcheck disable=SC2053
            if [[ ${tokens[$i-1]} == $level_pattern ]]; then

                local a=${tokens[i-2]}
                local op=${tokens[i-1]}
                local b=${tokens[i]}

                evaluate "$a" "$b" "$op"
                tokens[i-2]=$result

            else

                new_tokens[j]=${tokens[i]}
                new_tokens[j-1]=${tokens[i-1]}
                ((j-=2))
            
            fi

            ((i-=2))

        done

    fi

    new_tokens[j]=${tokens[i]}
    tokens=("${new_tokens[@]}")

}

function evaluate_flat {

    tokens=("$@")

    level_pattern="^"
    level_order=rtl
    evaluate_level

    level_pattern="[*/]"
    level_order=ltr
    evaluate_level

    level_pattern="[+-]"
    level_order=ltr
    evaluate_level

    result=${tokens[0]}

}

function evaluate_nested {

    local outer=() inner=() depth=0

    for token in "$@"; do

        case $token in
            
            "(") ((depth++));;
            
            ")") 
                ((depth--))

                if [[ $depth -eq 0 ]]; then

                    evaluate_nested "${inner[@]}"
                    outer+=("$result")
                    inner=()
                
                fi
            ;;

            *)
                if [[ $depth -eq 0 ]]; then
                    outer+=("$token")
                else
                    inner+=("$token")
                fi
            ;;

        esac
    
    done

    evaluate_flat "${outer[@]}"
}

function check_bracket {

    if [[ $index -ge ${#text} ]]; then
        return 1
    fi

    if [[ "${text:index:1}" == [\(\)] ]]; then
        tokens+=("${text:index:1}")
        ((index++))
    fi

    return 0

}

function collect_number {

    if [[ $index -ge ${#text} ]]; then
        return 1
    fi

    number=""

    while [[ (index -lt ${#text}) && (${text:index:1} == [0123456789]) ]]; do
        number+=${text:index:1}
        ((index++))
    done

    tokens+=("$number")
    return 0

}

function collect_operator {

    if [[ $index -ge ${#text} ]]; then
        return 1
    fi

    tokens+=("${text:index:1}")
    ((index++))
    return 0

}

function evaluate_expression {
    text="$1"
    index=0
    tokens=()

    while 
        check_bracket &&\
        collect_number &&\
        check_bracket &&\
        collect_operator
    do true; done

    evaluate_nested "${tokens[@]}"
}

evaluate_expression "$1"
echo $result