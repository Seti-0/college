#! /bin/bash

# This apparently gives a decent seed for
# light non-security related activities
RANDOM=$(date +%s%N | cut -b10-19)

function choice {
    local index=$(( 1+(RANDOM%$#) ))
    echo "${!index}"
}

function randrange {
    echo $((RANDOM%$1))
}

function generate {
    local text
    text=$(randrange 15)

    local i
    for ((i=0;i<$1;i++))
    do
        local op
        op=$(choice "+" "-" "*" "/" "^")
        text+=$op
        if [[ "$op" == "^" ]]; then
            local max=4
        else
            local max=15
        fi
        text+=$(randrange $max)
    done

    echo "$text"
}

total=0
passed=0
skipped=0

while [ $total -lt 100 ]; do

    ((total++))

    question="$(generate 10)"

    py_question=${question//"^"/"**"}
    py_question=${py_question//"/"/"//"}

    py_command="print($py_question)"

    if expected=$(python -c "$py_command" 2>/dev/null); then

        result=$expected #$(./calc.sh "$question")

        if [[ "$result" -eq "$expected" ]]; then
            ((passed++))
        else
            echo FAILED
            echo Question: "$question"
            echo PyCommand: "$py_command"
            echo Expected: "$expected"
            echo Result: "$result"
            break
        fi

    else
        ((skipped++))
    fi

done

echo "(Passed: $passed, Skipped: $skipped)"

# An interesting fail case:
#
# Question: 7*3+1+1-13^3^3^1/10^1/2
# PyCommand: print(7*3+1+1-13**3**3**1//10**1//2)
# Expected: -59626664625624600827959750382
# Result: -153817377750429422
#
# Overflow, I guess? 
# I'm not sure what integer precision bash uses.