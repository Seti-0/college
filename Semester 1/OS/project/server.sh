#! /bin/bash

pipeName="server.pipe"

if [ ! -e "$pipeName" ]; then
    mkfifo "$pipeName"
else
    echo "$pipeName already exists!" >&2
    exit 1
fi

echo "Starting server"
echo "Listening to $pipeName"

while read -ra words < server.pipe; do
    
    if [ "${#words[@]}" -lt 1 ]; then
        echo "Incoming request must have a client ID" >&2
        continue
    elif [ "${#words[@]}" -lt 2 ]; then
        echo "Incoming request must have a command" >&2
        continue
    fi

    echo "Incoming request: ${words[*]}"

    clientID="${words[0]}"
    command="${words[1]}"
    args=("${words[@]:2}")

    outputPipe="${clientID}.pipe"

    echo " - Client: $clientID"
    echo " - Output pipe: $outputPipe"
    echo " - Command: $command"
    
    for arg in "${args[@]}"; do
        echo "    - Argument: $arg"
    done

    if [ ! -p "$outputPipe" ]; then
        echo "Client pipe not found" >&2
        continue
    fi

    case "$command" in

        "create")
            ./create.sh "${args[@]}" &
        ;;
    
        "add")
            ./add.sh "${args[@]}" &
        ;;
    
        "post")
            ./post.sh "${args[@]}" &
        ;;
    
        "show")
            ./show.sh "${args[@]}" &
        ;;

        "shutdown")
            echo "Shutting down"
            break
        ;;

        *) echo "Unrecognized command: $command" ;;

    esac &> "$outputPipe"

    echo "Request processed"

done

echo "Deleting $pipeName"
rm "$pipeName"

echo "Shutting down"