"""

number = (user input)

for i in 1 to number (inclusive) do

    for j in 1 to number (inclusive) do
        
        (print i*j)

    end for

end for

"""

# I put a little bit of formatting into this one
print("===========================")
print("== Multiplication Tables ==")
print("===========================")

# Get the user input. The program will crash if
# the input is not an int.
generator = int(input("Enter number: "))

# Constants: cell width and left/right margin
# To keep things simple, the width is not made adaptive
width = 5
margin = 1

# Table border top
print("="*(width*generator+2*margin))

for i in range(1, generator + 1):

    for j in range(1, generator + 1):
        print(str(i*j).rjust(width), end="")

    # New line at the end of each row
    print()

# Table border bottom
print("="*(width*generator+2*margin))