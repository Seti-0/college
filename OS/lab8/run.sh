#!/bin/bash

if [ $# -ne 1 ]; then
	echo "This script requires exactly one argument"
	exit 1
fi

A="data_files/$1_available"
B="data_files/$1_allocated"
C="data_files/$1_requests"

if [ ! -e "$A" ]; then
	echo "Unable to find file: $A"
	exit 1
elif [ ! -e "$B" ]; then
	echo "Unable to find file: $B"
	exit 1
elif [ ! -e "$C" ]; then
	echo "Unable to find file: $C"
	exit 1
fi

./banker.sh "$A" "$B" "$C"
