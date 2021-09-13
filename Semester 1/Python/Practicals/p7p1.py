''' (Pseudocode)

(From lecture notes)

year = (user input)

if year >= 0:

    if (year mod 4 is 0) 
        and (year mod 100 is not 0)
        or (year mod 400 is 0):

        print "year is leap"

    else:
        print "year is not leap"

'''

year = int(input("Enter year: "))

leap = False

if year >= 0:

    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        print("Leap year!")
    else:
        print("Common year.")

else:
    print("Year must be non-negative")

