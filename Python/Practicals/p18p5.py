import re

"""
function passes(text):
    
    pattern = "(?<!\.)xyz"
    perform regex search
    
    return (search successful)

end function
"""

def passes(text):
    """Returns whether or not the text contains the string
        "xyz", not preceeded by a period."""

    match = re.search("(?<!\.)xyz", text)
    return match is not None


text = input("Enter text: ")
print(passes(text))
