#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: create NAME" >&2
    exit 1
fi

user=$1

if [ -d "$user" ]; then
    echo "User \"$user\" already exists" >&2
    exit 1
fi

if mkdir "$user"; then
    echo "User \"$user\" has been created"
    touch "$user/friends" "$user/wall"
else
    echo "Error while attempting to create user \"$user\""
fi