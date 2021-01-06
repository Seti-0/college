#!/bin/bash

if [ $# -ne 1 ]
then
	echo "Not one!" >&2
	exit 1
else
	echo "Good, good, one!"
fi
