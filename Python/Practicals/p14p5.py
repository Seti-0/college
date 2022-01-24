"""
function fibonnacci(n: non-negative int) 

    if n is (1 or 2) then return 1

    else return fibonnacci(n - 1) + fibonnacci(n - 2)

end function

(begin infinite loop)

    number = (user input)

    (if number is <= 0, exit)

    (print fibonnacci(number))

(end infinite loop)
"""

indent = 0

def fibonnacci(n):

    global indent

    print("  "*indent+"Input:", n)
    indent += 1

    if n == 1 or n == 2:
        answer = 1
    else:
        answer = fibonnacci(n - 1) + fibonnacci(n - 2)

    indent -= 1
    print("  "*indent+"Ouput:", answer)
    
    return answer

while True:

    number = int(input("Enter number: "))

    if number <= 0:
        print("Exiting")
        break

    print(fibonnacci(number))