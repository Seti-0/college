"""
function f(n: non-negative integer)

    if n is 1 then return 2

    else return n + f (n - 1)

end function

(begin infinite loop)

    number = (user input)

    (exit if number is non-positive)

    (print f(number))

(end infinite loop)
"""

def f(n):

    print("input:", n)

    if n == 1:
        answer = 2
    else:
        answer = n + f(n - 1)

    print("output:", answer)
    return answer

while True:

    number = int(input("Enter number: "))

    if number <= 0:
        print("Exiting")
        break

    print(f(number))