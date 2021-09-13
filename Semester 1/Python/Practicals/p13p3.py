"""
function print_max

    function max(a, b)

        if a > b then
            return a
        else
            return b
        end if

    end function

    (user input: number1, number2)

    (print max(number1, number2))

end function

print_max()
"""

def print_max():
    """Asks a user for two numbers, then prints out 
        the max of them"""

    def max(a, b):
        """Returns the max of two numbers"""
        if a > b:
            return a
        else:
            return b

    number1 = float(input("Enter number: "))
    number2 = float(input("Enter number: "))
    print("The largest of", number1, "and", number2, "is",
            max(number1, number2))

print(print_max)