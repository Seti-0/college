"""

number = (user input)

if number is 0 then

    (print answer: 1)

else

    total = 1

    for i in 1 to number (inclusive)
        total *= i

    end for

    (print answer: total)

end if

"""

# Promt the user for input. This will cause
# the program to crash if the input is not precisely 
# an integer
number = int(input("Enter number: "))

# We need the input to be non-negative
while number < 0:
    print("Number must be positive or zero")
    number = int(input("Enter number: "))

if number == 0:
    # Special case for zero
    print("The factorial of 0 is 1")

else:

    total = 1

    for i in range(1, number+1):
        total *= i

    print(f"The factorial of {number} is {total}")