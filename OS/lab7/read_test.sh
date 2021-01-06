#!/bin/bash

if [[ $# -ne 1 ]]; then
	echo "This script requires one argument: the input pipe"
	exit 1
fi

while true; do
	read item < $1
	echo "Message for you sire: $item"
done
