#! /bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: V.sh FILENAME">&2
    exit 1
fi

filename="$1"

if [ ! -e "$filename" ]; then
    echo "File '$filename' does not exist">&2
    exit 1
elif ! rm "${filename}.lock"; then
    echo "Unable to delete ${filename}.lock">&2
    exit 1
fi