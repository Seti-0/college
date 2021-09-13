"""

number = (user input)

total = 0
current = 1

while current <= number do

    total += current
    current++

end while

"""

# Promt the user for input. This will cause
# the program to crash if the input is not precisely 
# an integer
number = int(input("Enter number: "))

# We need the input to be positive
while number <= 0:
    print("Number must be positive")
    number = int(input("Enter number: "))

total = 0
current = 1

while current <= number:
    total += current
    current += 1

print(f"Sum of integers 1 to {number} is {total}")