"""

number = (user input)

a = 1
b = 1

if number > 0 then

    (print a)

end if

if number > 1 then 

    (print b)

end if

count = 2
while count < number do

    (b, a) = (a + b, b)

    (print b)

    count++

end while

"""

# Promt the user for input. This will 
# cause the program to crash if the user is
# not an integer
number = int(input("Enter number: "))

# Hard code the first 2 terms, the rest
# can be calculated using a recursion relation.

a = 1
b = 1

if number > 0:
    print(a)

if number > 1:
    print(b)

# Note that the loop counter is starting at 
# 2, not 0. The numbers printed by it are the third 
# and up
count = 2

while count < number:
    b, a = a + b, b
    print(b)
    count += 1

