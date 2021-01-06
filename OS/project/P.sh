#! /bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: P.sh FILENAME" >&2
    exit 1
fi

filename=$1

if [ ! -e "$filename" ]; then
    echo "File '$filename' does not exist" >&2
    exit 1
fi

while true; do
    if ln "$filename" "${filename}.lock" 2>/dev/null; then
        break
    fi
done
