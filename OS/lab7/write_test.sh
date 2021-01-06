#!/bin/bash

if [[ $# -ne 1 ]]; then
	echo "one argument required: the output pipe"
	exit 1
fi

while true; do
	read input
	echo "Sending message"
	echo "$input" > $1
done

