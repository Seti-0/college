"""

(start infinite loop)

    number = (user input)

    if number is negative then 

        exit loop
    
    else if number is 0 then

        (print answer: 1)

    else

        total = 1
        current = 1

        while current <= total do

            total *= current

        end while

        (print answer: total)

    end if

(end infinite loop)

"""

while True:

    # Promt the user for input. This will cause
    # the program to crash if the input is not precisely 
    # an integer
    number = int(input("Enter number: "))

    if number < 0:
        # Allow the user to exit the program
        break

    elif number == 0:
        # Special case for zero
        print("The factorial of 0 is 1")

    else:

        total = 1
        current = 1

        while current <= number:
            total *= current
            current += 1

        print(f"The factorial of {number} is {total}")