"""
check for input file existance
(error message if it does not)

open input file for reading

function get_count(character)

    count occurances of character line by line
    return count

end function

pairs = [
    ["<", ">"],
    ...
    ["[", "]"]
]

for (a, b) in pairs

    print counts of a and b using get_count
    compare counts, print success/error message

end for

close input file
"""

import os, sys

input_path = "p19p3_input.html"

if not os.path.isfile(input_path):
    print("Input path does not seem to be a file!")
    print("Exiting")
    sys.exit(0)

input_file = open(input_path, "r")

def get_count(char):

    # The seek is important - it 
    # means we start reading the file
    # from the start each time.
    input_file.seek(0)

    total = 0
    for line in input_file:
        total += line.count(char)

    return total

pairs = [
    ["<", ">"], 
    ["(", ")"], 
    ["{", "}"], 
    ["[", "]"]
]

for a, b in pairs:
    
    print("=========")

    count_a = get_count(a)
    count_b = get_count(b)
    
    print(a, "-", count_a)
    print(b, "-", count_b)

    if count_a == count_b:
        print("MATCH")

    else:
        print("ERROR - these do not match!")

print("=========")

input_file.close()