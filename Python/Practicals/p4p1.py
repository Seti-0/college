
print("== Euro to Pound Converter ==")
user_input = input("Enter amount to convert: ")

try:
    user_input = float(user_input)

except:
    print("Unable to parse input as number")
    exit(0)

if user_input < 0:
    print("Cannot convert a negative number")
    exit(0)

euro_to_pound = 0.91
result = user_input * euro_to_pound
print(f"£{result}")