''' (Pseudocode)

password = "1234"

current = input("Enter password")

if current equals password:
    print (Success)
    (exit program)

print("Enter password 3 times")

pass = True

for i in [1,2,3]:
    if not ((user input) equals password):
        pass = False 

if pass:
    print (Success)
else:
    print (Fail)

'''

password = "1234"

current = input("Enter password: ")

if password == current:
    print("You have successfully logged in.")
    exit(0)

print("Sorry, the password is wrong.")
print("Please enter the correct password three times...")

passed = True

for i in [1,2,3]:
    promt = str(i) + ": "
    if not input(promt) == password:
        passed = False

if passed:
    print("You have successfully logged in.")
else:
    print("You have beed denied access.")



