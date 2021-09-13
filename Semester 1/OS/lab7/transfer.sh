#!/bin/bash

if [[ $# -ne 2 ]]; then
	echo "Two arguments must be supplied to this script"
	exit 1
fi

while true; do
	read item < $1
	echo "Transferring item: $item"
	echo $item > $2
done
