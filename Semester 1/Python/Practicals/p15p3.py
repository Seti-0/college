"""
function f(n)

    if n is 0 then return 8

    else if n is 1 then return 13

    else return f(n-2) + 13 * f(n-1)

end function

(infinite loop)

    (user input: number)

    (if number is negative, exit)

    print(f(number))

(end infinite loop)
"""

def f(n):
    if n == 0:
        return 13
    elif n == 1:
        return 8
    else:
        return f(n - 2) + 13 * f(n - 1)

while True:

    number = int(input("Enter: number: "))

    if number <= 0:
        print("Exiting")
        break

    print(f(number))