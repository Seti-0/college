import time
import os
import ctypes
import multiprocessing as mp
import psutil

"""
These are the functions being used as subjects for 
timing. They are being kept in a seperate file to
avoid locking up IPython indefinitely. 

I'm not sure why, but it seems that trying to run 
multiprocessing and pools on a function within the notebook
hangs. 

See:
https://stackoverflow.com/questions/47313732/jupyter-notebook-never-finishes-processing-using-multiprocessing-python-3

It's also possible to use inspection to write a function's
source to a file on the fly.
"""

def check_prime(num):
    
    t1 = time.perf_counter()
    
    res = False
    if num > 0:
        # check for factors
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            res = True
            # if input number is less than
            # or equal to 1, it is not prime
    
    t2 = time.perf_counter()
    time_taken = t2 - t1
    
    return res, time_taken


"""

These two functions are for part two of the assignment, 
in which I try to see what core is doing what.

"""


def init(array, single_core=False):
    global out
    out = array
    
    if single_core:
        psutil.Process().cpu_affinity([0])


def track_core(index):

    for i in range(10000):
        out[index + i] = time.perf_counter()
        out[index + 10000 + i] = ctypes.cdll.kernel32.GetCurrentProcessorNumber()
