#!/bin/bash

rm -f f1 f2 f3

./write.sh f1 f2 f3 & ./write.sh f1 f2 f3

wait #Wait on the bg process to finish so run_write exits only when both write processes are done
