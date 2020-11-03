"""
function simple_find(target, source: list of lines)

    (print "searching for" message)

    for each line in source
        if line contains target
            return line index
        end if 
    end for

    return -1

end function

function find(target, source: list of lines)

    result = simple_find(target, source)

    if result is -1
        for i from length of target to 5
            result = simple_find(target[0:i], source)
            if result is not -1
                break
            end if
        end for
    end if

    if result is -1
        print not found message
    else
        print source[result]
        print found message
    end

end function
    

file_path = (user input)

check that the file exists, message and exit if not

source = list of lines in file

while True

    target = (user input)
    if target is empty, break

    find(target, source)

end while
"""

minlength = 5

def simple_find(target, source):
    """Takes a list of strings and a search target, and returns
        the index of the first string in the list that contains or is
        the search target. If no result is found, returns -1."""

    print("Searching for", target, end="    ")
    print("length of s:", len(target), end="    ")
    print("minlength:", minlength)

    for i in range(len(source)):
        if target in source[i]:
            return i

    return -1

def find(target, source):
    """Takes a list of strings and prints the first
       string that contains target, or any prefix of target
       down to a minimum length of 5. If no result is found,
       prints a message to that effect. 
       
       If target has 5 or less characters, no prefixes will 
       be searched for"""

    result = simple_find(target, source)

    if result == -1:

        print("Didn't find", target+".", "Searching for prefixes...")

        for i in range(1, len(target)-minlength+1):
            result = simple_find(target[0:len(target)-i], source)
            if result != -1:
                break

    if result == -1:
        print("No results for", target)

    else:
        print(source[result])
        print("Found result for", target, "(or one of its prefixes)")



import os, sys

input_path = input("Enter path: ").strip()

if input_path == "":
    input_path = "lines.txt"

if not os.path.isfile(input_path):
    print("Input path does not seem to be a file!")
    print("Exiting")
    sys.exit(0)

source = list(open(input_path, "r"))

while True:

    target = input("Enter search term: ")

    if target.strip() == "":
        print("Exiting")
        break

    find(target, source)




    

