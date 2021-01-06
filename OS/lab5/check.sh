#!/bin/bash

if [ $# -ne 1 ]
then
	echo "There should be one argument"
	exit 1
fi

input_path="$1"
dir_path=$(dirname "$input_path")
file_name=$(basename "$input_path")

if ! [ -d "$dir_path" ]
then
	echo "The directory $dir_path does not exist!"
elif ! [ -f "$dir_path/$file_name" ]
then
	echo "The file $file_name does not exist in $dir_path!"
else
	echo "The file was found"
fi
