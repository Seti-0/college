''' (Pseudocode)

year = parse (user input)

if (4 does not divide year):
    print "year is common"

else if (100 does not divide year):
    print "year is leap"

else if (400 does not divide year):
    print "year is common"

else year is leap

'''

year = int(input("Enter year: "))

leap = False

if not (year % 4 == 0):
    print("Common year.")

elif not (year % 100 == 0):
    print("Leap year!")

elif not (year % 400 == 0):
    print("Common year.")

else:
    print("Leap year!")

