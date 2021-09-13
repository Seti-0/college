''' (Pseudocode)

a = parse(enter first number)
b = parse(enter second number)
c = parse(enter third number)

largest = (no value)

loop through a, b, c:

    if largest is (no value):
        largest = current

    else if odd and greater than largest:
         largest = current

    else skip current

end loop

if largest is (no value):
    (no odd numbers found, print error)

else:
    print largest

'''

a = int(input("Enter a first number: "))
b = int(input("Enter another number: "))
c = int(input("Enter a final number: "))

# I was going to set this to zero initially, but
# it then occured to me that the user could input
# negative numbers
largest = None

for x in [a,b,c]:
    if x % 2 == 1:
        if largest is None or x > largest:
            largest = x

if largest is None:
    print("No numbers were odd!")
else:
    print(largest)