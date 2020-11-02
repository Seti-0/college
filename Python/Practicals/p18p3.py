import re

"""
function my_count(text):
    
    pattern = "co[a-zA-Z]e"
    matches = (regex search on text)
    
    return length of matches

end function
"""

def my_count(text):
    """Returns the count of occurances of a substring
       coXd, where X can be replaced by and upper or lower
       case letter"""
    matches = re.findall("co[a-zA-Z]e", text)
    return len(matches)


text = input("Enter text: ")
print(my_count(text))
