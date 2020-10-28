"""

function f(n)

    if n == 1 then
        print 2
        return 2
    else
        answer = 2 * f(n - 1)
        print(answer)
        return answer
    end if

end function

(infinite loop)

    number = (user input)

    (break if number is non-positive)

    f(number)

(end infinite loop)

"""

def f(n):
    """ Prints the first n powers of two 
        (starting with 2^1 = 2)"""

    print("[PART C] input:", n)

    if n == 1:
        print(2)
        print("[PART C] return:", 2)
        return 2
    else:
        answer = 2*f(n - 1)
        print(answer)
        print("[PART C] return:", answer)
        return answer

while True:

    number = int(input("Enter number: "))

    if number <= 0:
        print("Exiting!")
        break

    f(number)