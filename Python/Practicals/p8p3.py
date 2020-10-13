"""

number = (user input)

for i in 1 to 20

    (print i)

    (print i*number)

"""

# This is partially copied from p8p2
print("===========================")
print("== Multiplication Tables ==")
print("===========================")

# Get the user input. The program will crash if
# the input is not an int.
generator = int(input("Enter number: "))

# We can afford a larger width since there are
# only two columns. It is still not adaptive.
width = 8
margin = 1

# Table border top
print("="*(2*width+2*margin))

for i in range(1, 21):

        answer = str(i*generator).rjust(width)
        index = str(i).rjust(3)

        # Vertical bars for vertical borders
        print (f"| {index} | {answer} |")

# Table border bottom
print("="*(2*width+2*margin))