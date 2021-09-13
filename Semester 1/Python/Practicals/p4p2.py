import math

print("== Area Calculator ==")
user_input = input("Enter side length / diameter: ")

try:
    user_input = float(user_input)

except:
    print("Unable to parse input as number")
    exit(0)

if user_input < 0:
    print("A length cannot be negative")
    exit(0)

L = user_input

print("Square: "+str(L**2))
print("Cube: "+str(L**3))

R = L / 2
pi = math.pi

print("Circle: "+str((R**2)*pi))
print("Sphere: "+str((4/3)*(R**3)*pi))
print("Cylinder: "+str((R**2)*pi*L))

print("====")