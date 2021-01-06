#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: show USERNAME" >&2
    exit 1
fi

user=$1

if [ ! -d "$user" ]; then
    echo "User \"$user\" does not exist" >&2
    exit 1
fi

cat "$user/wall"