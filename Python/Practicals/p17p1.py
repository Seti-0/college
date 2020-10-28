"""

function divisors(n)

    divisors = (1,)

    for i from 2 to floor(n/2)
        if i divides n
            append i to divisors
        end if
    end for

    return diviors

end function

n = (user input)
(require a and b positive)
print(divisors(n))

"""

def divisors(n):
    """Returns a tuple of proper divisors of n"""

    result = (1,)
    for i in range(2, n//2):
        if n % i == 0:
            result += (i,)

    return result

n = int(input("Enter a number: "))

if n > 0:
    print(divisors(n))

else:
    print("The number must be positive")