"""
function is_perfect(n)

    total = 0
    for i from 0 to n - 1
        if n % i == 0:
            total += i
        end if
    end for

    return total == n

end

N = (user input)
(require N positive)

for n from 1 to N
    if is_perfect(n):
        print(n)
    end if
end for
"""

def is_perfect(n):
    """ 
        Returns true if n is a perfect number, else
        returns false. 

        Here, a perfect number is definied as one
        which is equal to the sum of its proper
        factors.
    """

    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i

    return total == n

N = int(input("Enter number: "))

if N <= 0:
    print("Number must be positive")

else:
    print("Printing perfect numbers:")

    for n in range(1, N+1):
        if is_perfect(n):
            print(n)

    print("Done!")