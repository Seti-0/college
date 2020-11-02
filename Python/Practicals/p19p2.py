"""
source = (user input)
source_base = (user input)

require that source base be positive and
less than 63

total = 0
power = len(source)

for character in source

    value = (index of digit represented by character)
    total += value * (source_base ^ power) 
    power--

end for

print total
"""

import sys

source = input("Enter number: ")
source_base = int(input("Enter base: "))

if source_base < 1:
    print("Base must be positive")
    sys.exit(0)

if source_base > 62:
    print("Base cannot be greater than 62")
    sys.exit(0)

chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
chars = chars[0:source_base]

powers = reversed(range(len(source)))
total = 0

for char, power in zip(source, powers):
    
    value = chars.find(char)
    
    if value == -1:
        print("Unrecognized character", char, "in input: ", source)
        sys.exit(0)

    total += value * (source_base ** power)

print(total)

