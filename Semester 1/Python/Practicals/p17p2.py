"""

function cd(a, b)

    divisors = (1,)

    for i from 2 to floor(min(a,b)/2)
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
    """ Returns a list of common proper divisors of
        two positive integers a and b"""

    result = (1,)
    for i in range(2, min(a, b)//2):
        if a % i == 0 and b % i == 0:
            result += (i,)

    return result

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

if a > 0 and b > 0:
    print(cd(a, b))

else:
    print("Both numbers must be positive")