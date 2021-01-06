#!/bin/bash

rm -f f1 f2 f3

./write.sh f1 f2 f3 & ./write.sh f1 f2 f3
