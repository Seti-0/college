#!/bin/bash

if [ $# -eq 1 ]; then

	if [ ! -e "$1" ]; then
		touch "$1"
	fi

	while true; do
		if ln "$1" "$1".sh; then
			break
		fi
	done

else

	echo "This script requires a single argument"
	exit 1

fi
