"""
function max(a: number, b: number)

    if a > b then
        return a
    else 
        return b
    end if

end function

(user input: number1, number2)

biggest = max(number1, number2)

(print biggest)

"""

def max(a, b):
    """
    Function that returns the largest of its two arguments
    """

    if a > b:
        return a
    else:
        return b

    
number1 = float(input("Enter a number: "))
number2 = float(input("Enter a number: "))

biggest = max(number1, number2)

print("The largest of", number1, "and", number2, "is",biggest)
print("Finished")