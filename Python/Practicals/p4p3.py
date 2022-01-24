
print("== Tax Calculator (v2) ==")
user_input = input("Enter original amount: ")

try:
    user_input = float(user_input)

except:
    print("Unable to parse input as number")
    exit(0)

if user_input < 0:
    print("Ammount cannot be negative")
    exit(0)

original = user_input
tax_a = original * 0.6 * 0.135
tax_b = original * 0.4 * 0.23
total_tax = tax_a + tax_b
total = original + total_tax

print()
print(f"13.5% tax on 60%: {tax_a}")
print(f"23% tax on 40%: {tax_b}")
print()
print(f"Total tax: {total_tax}")
print()

print(f"Total amount: {total}")

print("====")