"""
for each number A in the range

    is_prime = True

    for each number B from 2 up to A

        if B divides A then
            is_prime = False
            (print pair)
        end if
    
    end foreach

    if is_prime then
        (it's a prime number)
        (inform the user)
    end if

end foreach
"""

for number in range(2, 20):

    is_prime = True

    # Note the number//2. This is to
    # avoid printing each pair out twice,
    # with the second one reversed.
    # 
    # i.e. for 18 = 3*6 there is no need
    # to print 18 = 6*3.
    for i in range(2, number//2):
        if number % i == 0:
            is_prime = False
            print(number, "equals", i, "*", number//i)

    if is_prime:
        print(number, "is a prime number")