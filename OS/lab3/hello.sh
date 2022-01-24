#!/bin/bash

if [ $# -eq 0 ]; then
	echo "Hello Sith Lord!"
fi

for name in "$@"; do
	echo "Hello $name!"
done

