''' (Pseudocode)

password = "1234"

attempts = 0

while attempts < 3:
    
    input = (user input)
    
    if input equals password:
        print success
        (exit program)

    attempts++

end while

print error

'''

password = "1234"

attempts = 0

while attempts < 3:
    text = input("Enter password: ")
    if text == password:
        print("You have successfully logged in")
        exit(0)
    attempts += 1

print("You have been denied access")

