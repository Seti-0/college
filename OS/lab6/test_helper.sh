#!/bin/bash

#This script is here to help with github tests. Do not modify.

case $1 in
        1)
               ./P.sh P.sh
               timeout 2s ./P.sh P.sh
               if [ $? -eq 124 ]; then
                       exit 0 
               else
                       echo "Could enter the semaphore twice in a row (2 Ps without V)"
                       exit 1
               fi
               ;;
       2)
               files="$(ls -l)"
               ./P.sh P.sh
               ./V.sh P.sh
               if [ "$(ls -l)" = "$files" ]; then
                       exit 0
               else
                       echo "V did not delete the lock correctly"
                       exit 1
               fi
               ;;
       3)
               ./P.sh P.sh
               ./V.sh P.sh
               timeout 2s ./P.sh P.sh
               if [ $? -eq 124 ]; then
                       echo "Could not reenter semaphore after unlock (could not do P V P)"
                       exit 1
               else
                       exit 0
               fi
               ;;
       *)
               ;;
esac
