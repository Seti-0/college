number = int(input("Please input a number: "))

if number == 0:
    print("Number is equal to 0")

elif number < 0:
    print("Number is less than 0")

elif number > 100:
    print("Number is greater than 100")

else:
    # There is a subtlety with this formula
    # where "number - 1" is concerned, see footnote
    a = int((number - 1) / 20) * 20
    b = a + 20

    print(f"Number is greater than {a} "
        + f"and less than or equal to {b}")


# I thought I was being clever by typing:
#   
#   a = int(number / 20) * 20
#   b = a + 20
#
# However, this gives values a,b such that 
# "number" falls in the range [a,b)
#
# The question is asking for values a,b such that 
# "number" falls in the range (a,b]. In other words,
# the above solution fails when "number" exactly a or b.
#
# A fix to the formula is to subtract one from the number.
# This only works because the number is an integer though
#
# At this point, it would have been quicker just to type out
# the elifs!
