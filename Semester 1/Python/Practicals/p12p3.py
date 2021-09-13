"""
(Part a)

function root(x: non-negative float)

    (use exhaustive enumeration to return the root of x)

end function


(Part b)

number = (user input)

if number is negative then

    (print error)

else 

    (print root(number))

end if
"""

def root(n: float):

    # This method is from lecture 12 slide 10.

    # Find the result to about 3 decimal places
    eps = 1e-3

    # An extra order of magnitude is fine here, squaring
    # it seems a bit much
    step = 1e-4
    
    current = 0

    while abs(current**2 - n) > eps and current**2 <= number:
        current += step

    return current

number = int(input("Enter number: "))

if number < 0:
    print("Number must be positive")

else:
    print(root(number))