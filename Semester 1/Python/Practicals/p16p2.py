"""

function cd(a, b)

    divisors = (empty list)

    for i from 1 to min(a,b)
        if i divides a and b then
            append i to divisors
        end if
    end for

    return diviors

end function

a, b = (user input)
(require a and b positive)
print(cd(a, b))

"""

def cd(a, b):
    """ Returns a list of common divisors of
        two positive integers a and b"""

    result = []
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            result.append(i)

    return result

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

if a > 0 and b > 0:
    print(cd(a, b))

else:
    print("Both numbers must be positive")