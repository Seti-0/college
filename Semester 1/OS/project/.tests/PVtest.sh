#! /bin/bash

# Unlike PVcontrol.sh, the output from this script should
# not be mixed up, since there is a locking mechanism

function bar 
(
    ./P.sh "$0"
    for ((i=0;i<30;i++)); do
        printf "%s" "$1"
    done
    ./V.sh "$0"
)

for ((i=0;i<10;i++)); do
    bar "$i" &
done

printf "\n"
