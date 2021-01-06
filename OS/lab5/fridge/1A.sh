#!/bin/bash

# Solution 1: Real life, I guess

if [ ! -s milk ]; then
	if [ ! -s note ]; then
		echo "Gone to get milk" >> note
		echo "1 Carton" >> milk
		echo "" >> note
	fi
fi
