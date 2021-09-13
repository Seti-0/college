"""
for each number A in the range

    for each number B from 2 up to A

        if B divides A then
            (it's not a prime number)
            (inform the user)
            (break)
        end if
    
    end foreach

    if the loop fell through then
        (it's a prime number)
        (inform the user)
    end if

end foreach
"""

for number in range(2, 20):
    for i in range(2, number):
        if number % i == 0:
            print(number, "equals", i, "*", number//i)
            break
    else:
        print(number, "is a prime number")