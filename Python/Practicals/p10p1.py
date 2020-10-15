"""

number = (user-input)

answer = (no value)

for i from 0 to number do

    if i^2 is number then

        answer = i
        (exit loop)

    end if

end for

if answer is (no value) do

    (print error)

else

    (print answer)

end if

"""

# Promt the user for input. This will
# cause the program to crash if the input
# is not an integer
number  = int(input("Enter number: "))

# Use 'None' as a placeholder to indicate
# that no answer has been found yet
answer = None

for i in range(number+1):
    if i**2 == number:
        answer = i
        # The answer has been found, there is no further
        # need to search for solutions
        break

if answer is None:
    print("This number is not a perfect square.")
else:
    print(f"The root of your number is {answer}")


