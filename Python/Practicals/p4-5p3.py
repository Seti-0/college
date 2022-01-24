
# This program is almost identical to p4p3
print("== Tax Calculator (v3) ==")
user_input = input("Enter original amount: ")

try:
    user_input = float(user_input)

except:
    print("Unable to parse input as number")
    exit(0)

if user_input < 0:
    # The error message is different
    print("Amount of income must be >= 0. Please try again.")
    exit(0)

original = user_input
tax_a = original * 0.6 * 0.23
tax_b = original * 0.4 * 0.41
total_tax = tax_a + tax_b
total = original + total_tax

print()
print(f"23% tax on 60%: {tax_a}")
print(f"41% tax on 40%: {tax_b}")
print()
print(f"Total tax: {total_tax}")
print()

print(f"Total amount: {total}")

print("====")