"""
function is_suffix(a, b)
    
    set a and b to lower
    
    return (a ends with b) or (b ends with a)

end function
"""

def is_suffix(a, b):
    """Returns true if a ends in b or b ends in a. 
       Returns false otherwise. Ignores case."""
    a, b = a.lower(), b.lower()
    return a.endswith(b) or b.endswith(a)


a = input("Enter text: ")
b = input("Enter more text: ")

print(is_suffix(a, b))

    