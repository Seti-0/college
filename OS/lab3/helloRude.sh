#!/bin/bash

if [ $# -eq 0 ]; 
then
	echo "Hello Sith Lord!"
else
	for ((i=1;i<=$#;i++));
	do
		if [ $((i%2)) -eq 0 ];
		then
			echo "Hello ${!i}!"
		fi
	done
fi
