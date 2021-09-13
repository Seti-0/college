"""

function count_code(text)

    return text.count("code")

end function

"""

def count_code(text):
    """Returns the count of occurances of "code"  in the 
        specified text"""
    return text.count("code")


text = input("Enter text: ")
print(count_code(text))