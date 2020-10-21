"""
(Part a)

function factorial(n: non-negative integer)

    total = (calculate factorial)
    return total

end function


(Part b)

number = (user input)

if number is negative then

    (print error)

else

    answer = factorial(number)
    (print answer)

end if
"""

def factorial(n: int):

    total = 1
    
    for i in range(1, n+1):
        total *= i
    
    return total

number = int(input("Enter number: "))

if number < 0:
    print("Number must not be negative")

else:
    answer = factorial(number)
    print(answer)

