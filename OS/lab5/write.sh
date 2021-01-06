#!/bin/bash

if [ $# -lt 1 ]; then

	echo "This script requires at least one argument"
	exit 1

fi

for elem in "$@" ; do
	# Critical section
	if [ ! -e "$elem" ] ; then
		echo "Process $$ got here first" >> "$elem"
	else
		echo "Someone came before process $$" >> "$elem"
	fi
	# End critical section
done
