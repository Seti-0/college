#!/bin/bash

if [ $# -eq 0 ]; then
	echo "Good luck Sith Lord!"
fi

for name in "$@"; do
	echo "Good luck $name!"
done

