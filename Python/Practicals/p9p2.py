"""

(start infinite loop)

    number = (user input)

    total = 0

    for i in range(1, number+1)
    
        total += i

    end for

(end infinite loop)

"""

while True:

    # Promt the user for input. This will cause
    # the program to crash if the input is not precisely 
    # an integer
    number = int(input("Enter number: "))

    # Allow the user to end the program by entering
    # a non-positive number
    if number <= 0:
        break

    total = 0

    for i in range(1, number+1):
        total += i

    print(f"Sum of integers 1 to {number} is {total}")