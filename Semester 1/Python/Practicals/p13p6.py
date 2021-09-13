"""
Part a)

function factorial(n: non-negative integer)

    if n is 0 then
        return 1
    else
        return n * factorial(n - 1)
    end

end function

Part b)

(user input: number)

if number is negative then

    (print error)

else

    (print factorial(number))

end if
"""

def factorial(n: int):
    
    print("Requested", str(n) + "!")

    if n == 0:
        answer = 1
    else:
        answer = n * factorial(n - 1)

    # For part c), print this
    # as well as returning it
    print("Returned", answer)

    return answer

number = int(input("Enter number: "))

if number < 0:
    print("Number must be greater than 0")
else:
    print("Result: ", factorial(number))