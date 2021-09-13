#! /bin/bash

echo "" > joe/friends

for ((i=0;i<20;i++)); do

    ./client.sh id"$i" add joe anne &

done