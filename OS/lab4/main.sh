#!/bin/bash

if [ $# -eq 0 ];
then

	echo "no argument given"

else

	for ((i=1;i<=$#;i++))
	do
		if grep -qx "${!i}" goodies;
		then

			./welcome.sh "${!i}"

		elif grep -qx "${!i}" baddies;
		then

			./wereFull.sh "${!i}"

		else

			./iDontKnowYou.sh "${!i}"
		fi
	done
fi
