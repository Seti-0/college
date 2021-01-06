#! /bin/bash

if [ $# -lt 3 ]; then
    echo "Usage: post.sh RECEIVER SENDER MESSAGE..." >&2
    exit 1
fi

reciever=$1
sender=$2

shift 2
message="$*"

if [ ! -d "$reciever" ]; then
    echo "User \"$reciever\" does not exist" >&2
    exit 1
elif [ ! -d "$sender" ]; then
    echo "User \"$sender\" does not exist" >&2
    exit 1
fi

if [[ "$sender" = "$reciever" ]] ||\
     grep -qFx "$sender" "$reciever/friends"; then

    message="${sender}: $message"

    ./P.sh "$reciever/wall"
    status=0

    if echo "$message" >> "$reciever/wall"; then
        echo "Message appended to the wall of \"$reciever\""
    else
        echo "Failed to write message to the wall of \"$reciever\""
        status=1
    fi
    ./V.sh "$reciever/wall"

    exit $status

else

    echo "$sender is not a friend of $reciever" >&2
    exit 1

fi
