"""

number = (user input)

if number < 0 then

    (print error and exit)

else

    total = 1

    (This loop 
    should not execute if number is 0)
    for i from 1 to number do

        total = total * i

    end for

    (print answer: total)

end if

"""

number = int(input("Enter number: "))

if number < 0:
    print("Error: number was less than zero")

else:

    # The key is that regardless of whether 
    # number is 0, 1 or greater than 1, fact
    # will always be set initially to 1
    fact = 1

    # Then: 
    #   - in the 0 case the range will
    #     be range(1,1) which has no values.
    #   - in the 1 case the range will be
    #     be range(1,2). i will take the value 1
    #     only and fact will remain unchanged.
    for i in range(1, number+1):
        fact *= i

    # For the case number > 1, the code is unchanged
    # from the lecture example. So the overall affect
    # is that the same result is achieved with 
    # a single if statement.
    print("The factorial is", fact)
