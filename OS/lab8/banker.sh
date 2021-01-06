#!/bin/bash

##check arguments
if [ ! $# -eq 3 ]; then
        echo "This script requires 3 arguments" >&2
        echo "usage: $0 available_resources_file allocated_resources_file requested_resources_file" >&2
        exit 1
elif [ ! -e "$1" ]; then 
        echo "available resources file not found" >&2
        exit 1
elif [ ! -e "$2" ]; then 
        echo "allocated resources file not found" >&2
        exit 1
elif [ ! -e "$3" ]; then
        echo "requested resources file not found" >&2
        exit 1
fi


##data validation
if [ ! $(wc -l "$1" | cut -d" " -f1) -eq 1 ]; then
        echo "available resources file not formatted properly: should contain only one line" >&2
        exit 1
fi
numResources=$(wc -w "$1" | cut -d" " -f1)

echo "There are $numResources resources in this problem"

if [ ! $(wc -l "$2" | cut -d" " -f1) -eq $(wc -l "$3" | cut -d" " -f1) ]; then
        echo "allocated resources file or requested resources file not formatted properly: should have the same number of processes (lines)" >&2
        exit 1
fi

numProcesses=$(wc -l "$2" | cut -d" " -f1)
echo "There are $numProcesses processes in this problem"

while read line; do
        if [ ! $(echo "$line" | wc -w | cut -d" " -f1) -eq $numResources ]; then
                echo "allocated resources file not formatted properly: all lines should have the same number of resources as the available resources file" >&2
                exit 1
        fi
done < "$2"

while read line; do
        if [ ! $(echo "$line" | wc -w | cut -d" " -f1) -eq $numResources ]; then
                echo "requested resources file not formatted properly: all lines should have the same number of resources as the available resources file" >&2
                exit 1
        fi
done < "$3"

loopDone=false

unfinished=($(seq 1 $numProcesses))
avail=($(cat "$1"))

while [ "$loopDone" = false ] ; do
        loopDone=true
        for processId in "${unfinished[@]}"; do

		request=($(sed -n "${processId}p" < "$3"))
                canFulfillRequest=true

                for ((i=0;i<"${#avail[@]}";i++)); do

			if [ "${avail[i]}" -lt "${request[i]}" ]; then
				canFulfillRequest=false
				break
			fi

		done

                if [ $canFulfillRequest = true ]; then 
                        echo "Executing process $processId"

                        unset 'unfinished['$(($processId-1))']'

                        allocated=($(sed -n "${processId}p" < "$2"))

			for ((i=0;i<"${#avail[@]}";i++)); do
				avail[i]=$((avail[i]+allocated[i]))
			done
                        loopDone=false
		fi
	done
done

if [ ${#unfinished[@]} -eq 0 ]; then
        echo "The system is in a safe state"
else
        echo "The system is in an unsafe state"
fi
