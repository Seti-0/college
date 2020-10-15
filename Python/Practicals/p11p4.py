"""

number = (user input)

if number < 0 then

    (print error)

elif number > 0 then

    C = 1
    (print C)

    for n from 0 to (number - 1) do
        
        C = (2(2n+1)/(n+2))C
        (print C)

    end for

end if

"""

number = int(input("Enter number: "))

if number < 0:
    print("Number cannot be negative")

elif number > 0:

    C = 1
    print(C)
    
    for n in range(0, number - 1):
        
        # There is a sub
        # tlety to the use of the 
        # the // here, and that is that all factors 
        # must be present on the numerator in order
        # for the denominator to be guaranteed to
        # to divide in evenly.

        # The practical implication is that to keep
        # everything integer the order of operations
        # does matter, and the "*=" operator cannot
        # be used with the "//" operator.

        # Of course, floats would work too.

        C = (2*(2*n + 1)*C)//(n+2)
        print(C)