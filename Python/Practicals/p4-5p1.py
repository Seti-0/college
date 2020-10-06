# This program is almost identical to p4p1
print("== Euro to Pound Converter II ==")
user_input = input("Enter amount to convert: ")

try:
    user_input = float(user_input)

except:
    print("Unable to parse input as number")
    exit(0)

if user_input < 0:
    # The error message here is different
    print("Amount must be >= 0. Please try again.")
    exit(0)

# The exchange rate is still 0.91 to two decimal places
euro_to_pound = 0.91
result = user_input * euro_to_pound
print(f"£{result}")