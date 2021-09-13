"""
check for input file existance
(error message if it does not)

We don't need to check for the output file 
 - it will be overwritten if it exists, or created 
   if it does not, when we open it for writing

open input file for reading
open outfile for writing

function print_count(character)

    count occurances of character line by line
    write count to output

end function

for char in [">", ..., "-->"]
    print_count(char)
end for

close input and output files
"""

import os, sys

input_path = "p18p6_input.html"

if not os.path.isfile(input_path):
    print("Input path does not seem to be a file!")
    print("Exiting")
    sys.exit(0)

input_file = open(input_path, "r")
output_file = open("p18p6_output.txt", "w")

def print_count(char, name=None):

    # The seek is important - it 
    # means we start reading the file
    # from the start each time.
    input_file.seek(0)

    total = 0
    for line in input_file:
        # str.count() is case sensitive
        total += line.count(char)

    output_file.write(f"{name} - {total}\n")

for char in [">", "<", "e", "<!--", "-->"]:
    print_count(char, name=char)

# Don't just pass the newline character as the name,
# like the others. That would not be a helpful name.
print_count("\n", name="\\n")

input_file.close()
output_file.close()