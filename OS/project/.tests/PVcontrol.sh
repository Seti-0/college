#! /bin/bash

# Unlike PVtest.sh, the output of this should be
# mixed up, since there is no locking mechanism.

function bar 
(
    for ((i=0;i<30;i++)); do
        printf "%s" "$1"
    done
)

for ((i=0;i<10;i++)); do
    bar "$i" &
done

printf "\n"
