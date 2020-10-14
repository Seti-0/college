"""

(initialize counter variables)

(start infinite loop)

    number = (user input)

    if number is negative then
        
        exit loop

    end if

    if number is 0 then

        (counter 0)++

    else if number <= 20 then

        (counter 0 to 20)++

    ...

    else 

        (counter beyond 100)++

    end if

(end infinite loop)

(print counters)

"""

count_0 = 0
count_0_to_20 = 0
count_20_to_40 = 0
count_40_to_60 = 0
count_60_to_80 = 0
count_80_to_100 = 0
count_big = 0

while True:

    current = int(input("Enter number: "))

    if current < 0:
        break

    if current == 0:
        count_0 += 1
    
    elif current <= 20:
        count_0_to_20 += 1

    elif current <= 40:
        count_20_to_40 += 1

    elif current <= 60:
        count_40_to_60 += 1

    elif current <= 80:
        count_60_to_80 += 1

    elif current <= 100:
        count_80_to_100 += 1

    else:
        count_big += 1

print("   Zeros: " + str(count_0))
print(" (0, 20]: " + str(count_0_to_20))
print("(20, 40]: " + str(count_20_to_40))
print("(40, 60]: " + str(count_40_to_60))
print("(60, 80]: " + str(count_60_to_80))
print("(80,100]: " + str(count_80_to_100))
print("   Large: " + str(count_big))

