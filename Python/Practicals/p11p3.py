"""

(begin infinite loop)

    number = (user input)

    if number < 0 then

        (exit loop)

    end if

    if number == 0 then

        (skip to next iteration)

    end if

    a = 1
    
    (print a)

    if number == 1 then 

        (skip to next interation)

    end if

    b = 1

    (print b)

    loop (number - 2) times

        b, a = a + b, b
        
        (print b)

    end loop

(end infinite loop)

"""

while True:

    number = int(input("Enter number: "))

    if number < 0:
        break

    if number == 0:
        continue

    a = 1
    print(a)

    if number == 1:
        continue

    b = 1
    print(b)

    for _ in range(2, number):
        b, a = a+b, b
        print(b)
