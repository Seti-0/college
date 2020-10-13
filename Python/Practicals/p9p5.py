"""

n = (user input)
k = (user input)

(require n and k to be positive)

(require n to be greater or equal to k)

n_factorial = 1

for i in 1 to n (inclusive) do
    
    n_factorial *= i

end for


k_factorial = 1

for i in 1 to k (inclusive) do

    k_factorial *= i

end for

n_k_factorial = 1

for i in 1 to n - k (inclusive) do

    n_k_factorial *= i

end for

answer = n_factorial / (k_factorial * n_k_factorial)

(print answer)

"""

# Promt the user for input. This will cause
# the program to crash if the inputs are not precisely 
# integers
n = int(input("Enter count of available options: "))
k = int(input("Enter count to be chosen: "))

# There are a few possible errors we could print out here.
# Print them all, and only continue the program if none occur
valid_input = True

if n <= 0:
    print("Count of available options must be positive")
    valid_input = False

if k <= 0:
    print("Count chosen must be positive")
    valid_input = False

if n < k:
    print("Count of available options must be"
        + " greater than or equal to count chosen")
    valid_input = False

if valid_input:

    # Compute each of the three factorials individually

    n_factorial = 1
    for i in range(1, n+1):
        n_factorial *= i

    k_factorial = 1
    for i in range(1, k+1):
        k_factorial *= i

    n_k_factorial = 1
    for i in range(1, n-k+1):
        n_k_factorial *= i

    # The double // here is to keep things as integers
    answer = n_factorial / (k_factorial * n_k_factorial)

    print(f"There are {answer} possible combinations")

