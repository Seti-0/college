"""

x = (enter input)

if x < 0:
    print(error)

else:

    count_3 = 0
    ...
    count_11 = 0

    current = 1
    while current <= x:
        
        if current is divisible by 3:
            count_3++

        ...

        if current is divisible by 11:
            count_11++
        
        current++

"""

# Retrieve user input. This will throw a ValueError
# if the input is not a valid integer
x = int(input("Enter a non-negative integer: "))

print("You entered: " + str(x))

# Ignore negative integers
if x < 0:
    print("Number entered should be >= 0.")

else:

    # A loop is arguable neater than the repetition
    # here, but I am reluctant to be imaginative after the practicals

    count_3 = 0
    count_5 = 0
    count_7 = 0
    count_11 = 0

    # It is important to start at 1, not zero, since
    # using the modulus test below 0 is considered divisible by all
    # numbers
    current = 1
    while current <= x:

        if current % 3 == 0:
            count_3 += 1

        if current % 5 == 0:
            count_5 += 1

        if current % 7 == 0:
            count_7 += 1

        if current % 11 == 0:
            count_11 += 1

        current += 1

    print("Numbers divisible by 3: "+str(count_3))
    print("Numbers divisible by 5: "+str(count_5))
    print("Numbers divisible by 7: "+str(count_7))
    print("Numbers divisible by 11: "+str(count_11))

print("Finished!")
