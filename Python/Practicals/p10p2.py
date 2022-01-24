"""

(start infinite loop)

    number = (user input)

    if number is 0 then

        (exit loop)

    end if

    answer = (no value)

    (Note that this loop may have to step down, rather than up)
    for i from 0 to number do
        
        if i**3 is number then
    
            answer = i
            (exit loop)
    
        end if

    end for

    if answer is (no value) then

        (print error)

    else

        (print answer)

    end if

(end infinite loop) 

"""

while True:

    # This section similar to p10p1 

    number = int(input("Enter number: "))
    answer = None

    if number == 0:
        break

    if number >= 0:
        step = 1
        bound = number + 1
    else:
        step = -1
        bound = number - 1

    for i in range(0, bound, step):

        if i**3 == number:
            answer = i

    if answer is None:
        print("This number is not a perfect cube")
    else:
        print(f"The cube of the number is {answer}")
