"""
(Part a)

function fibonnacci(n: non-negative integer)

    (print out fibonnacci terms)

end function


(Part b)

number = (user input)

if number is negative then

    (print error)

else

    fibonnacci(number)

end if
"""

def fibonnacci(n: int):

    if n > 0:
        print(1)

    if n > 1:
        print(1)

    if n > 2:
        a = b = 1
        for _ in range(n-2):
            b, a = a + b, b
            print(b)

number = int(input("Enter number: "))

if number < 0:
    print("Number must be positive")
else:
    fibonnacci(number)
