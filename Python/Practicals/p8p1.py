"""

(start infinite loop)

    current = (user input)

    if current < 0 then
         
         exit loop

    end if

    for divisor in 2, 3, 5, 7 do

        if current is divisible by divisor then
            
            (print current is divisible by divisor)

        else

            (print current is not divisible by divisor)

        end if

    end for

(end infinite loop)

"""

while True:

    # Ask for input. If the input is not an int,
    # the program will crash here.
    current = int(input("Enter a number: "))

    # This is the only way the loop exits (other than crashing)
    if current < 0:
        break

    # Special case for 0, since it is not a valid input
    # to the modulus test for divisibility
    elif current == 0:
        print("0 is not divisible by any number")

    else:

        # No need to print this out 4 times
        print(f"{current} is:")

        for divisor in [2,3,5,7]:
            if current % divisor == 0:
                print(f" - divisible by {divisor}")
            else:
                print(f" - not divisible by {divisor}")