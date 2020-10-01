

# Our constant float represents the side length
L = 164988.02

print("Square: "+str(L**2))
print("Cube: "+str(L**3))

# For circles and sphere, L represents the diameter.
# However, the calculations are easier in terms of the radius
R = L / 2
pi = 3.1415927

print("Circle: "+str((R**2)*pi))
print("Sphere: "+str((4/3)*(R**3)*pi))

print("Cylinder: "+str((R**2)*pi*L))