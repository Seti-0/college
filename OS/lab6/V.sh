#!/bin/bash

if [ $# -eq 1 ]; then
	rm "$1".sh
else
	echo "This script requires a single argument"
fi
