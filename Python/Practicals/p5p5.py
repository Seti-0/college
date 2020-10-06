# x is a town or city
x = input("Enter town name: ")
# y is a province
y = None

if x in ["Dublin", "Kilkenny"]:
    y = "Leinster"

elif x in ["Cork", "Limerick", "Waterford"]:
    y = "Munster"

elif x in ["Galway", "Sligo"]:
    y = "Connacht"

elif x in ["Belfast", "Derry", "Lisburn"]:
    y = "Ulster"

if y is None:
    print("Sorry, I didn't recognize that name.")
else:
    print(f"You entered {x}, {x} is in {y}")