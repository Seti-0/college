'''
Created on 26 Jan 2021

@author: Kieran Cosson
'''

import socket, platform, multiprocessing
from psutil import virtual_memory

def hello(name = "World"):
    print(f"Hello {name}")
    

def print_info():
    
    print("Name:", socket.gethostname())
    print("OS Name:", platform.system(),
          platform.release())
    
    print("CPU count:", multiprocessing.cpu_count())
    print("Memory:", virtual_memory().total)