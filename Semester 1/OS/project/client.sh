#! /bin/bash

if [ $# -lt 1 ]; then
    echo "Usage: client.sh ID COMMAND ARGS..." >&2
    exit 1
fi

serverPipe="server.pipe"

clientID="$1"
clientPipe="${clientID}.pipe"

if [ -e "$clientPipe" ]; then

    echo "A file already exists with the name $clientPipe" >&2
    echo "Is a client already running with the same ID?" >&2
    exit 1

elif ! mkfifo "$clientPipe"; then

    # mkfifo will echo its own error message
    exit 1

fi

status=0

if [ ! -p "$serverPipe" ]; then
    echo "$serverPipe does not exist. Has the server been started?"
    status=1
else
    ./P.sh "$serverPipe"
    echo "$*" >> "$serverPipe"
    ./V.sh "$serverPipe"

    cat < "./$clientPipe"
fi

if ! rm "$clientPipe"; then
    echo "Warning: unable to delete $clientPipe" >&2
fi

exit "$status"
