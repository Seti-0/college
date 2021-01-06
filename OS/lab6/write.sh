#!/bin/bash

if [ $# -lt 1 ] ; then
    echo "This script requires at least one parameter"
    exit 1
fi
for elem in "$@" ; do
    ./P.sh "$elem"
    if [ ! -e "$elem" ] ; then
        sleep 1
        echo 1st $$ > "$elem"
    else
        echo next $$ >> "$elem"
    fi
    ./V.sh "$elem"
done
