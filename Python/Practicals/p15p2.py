"""
function f(n)

    if n is 1 then return 1

    else return f(n-1) + 2^(n-1)

end function

(infinite loop)

    (user input: number)

    (if number is non-positive, exit)

    print(f(number))

(end infinite loop)
"""

def f(n):

    print("input:",n)

    if n == 1:
        answer = 1
    else:
        answer = f(n - 1) + 2 ** (n - 1)

    print("ouput:", answer)
    return answer

while True:

    number = int(input("Enter: number: "))

    if number <= 0:
        print("Exiting")
        break

    print(f(number))