"""
function letters_only(text)

    text = (lower case of text)

    relevent = "abcdefghijklmnopqrstuvwxyz"
    result = (empty string)

    foreach char in text do
        if char is in relevant
            result += char
        end if
    end for

    return result

end function

function palindrome_helper(text)

    if length of text is 1 then
        return true
    else
        return text[0] == text[-1] and palindrome_inner(text[1:-2])


function is_palindrome(text):

    text = letters_only(text)
    return palindrome_inner(text)

end function

"""

def letters_only(text):
    """Returns the text in lower case stripped of all
       characters that are not in the english alphabet."""

    text = text.lower()
    relevant = "abcdefghijklmnopqrstuvwxyz"
    result = ""

    for char in text:
        if char in relevant:
            result += char

    return result

def palindrome_helper(text):
    """Returns true if the input is a palindrome, else false.
    
       Assumes the input is made up of characters of the english
       alphabet of constant case."""

    if len(text) == 1:
        return True

    else:
        return text[0] == text[-1] and palindrome_helper(text[1:-1])

def is_palindrome(text):
    """Returns true if the input is a palindrome, else false"""
    text = letters_only(text)
    return palindrome_helper(text)

while True:

    text = input("Enter text: ")

    if len(text.strip()) == 0:
        print("Exiting program")
        break

    if is_palindrome(text):
        print("This is a palindrome")
    
    else:
        print("This is not a palindrome")



