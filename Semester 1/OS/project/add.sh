#!/bin/bash

if [ $# -ne 2 ]; then
    echo "Usage: add USER FRIEND" >&2
    exit 1
fi

user=$1
friend=$2

if [ ! -d "$user" ]; then
    echo "No user with the name $user exists" >&2
    exit 1
elif [ ! -d "$friend" ]; then
    echo "No user with the name $friend exists" >&2
    exit 1
elif [ "$user" = "$friend" ]; then
    echo "User and friend cannot be the same person" >&2
    exit 1
fi

./P.sh "$user/friends"

# We should not exit until V.sh has been called
status=0

if grep -xqF "$friend" "$user/friends"; then

    echo "$friend is already a friend of $user" >&2
    status=1

elif echo "$friend" >> "$user/friends"; then

    echo "$friend has been added as a friend of $user"
    status=0

else

    echo "Failed to add $friend as a friend of $user"
    status=1

fi

./V.sh "$user/friends"

exit $status

