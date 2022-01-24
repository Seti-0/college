"""
function letters(text)

    result = (empty string)

    for each character in text
        if character is letter or space
            append character to result
        end if
    end for

    return result

end function

function is_palindrome(text)

    result = True

    for i from 1 to floor((length of text)/2)
        if text[i] != text[i-1]
            result = False
        end if
    end for

    return result

end function

while True 

    text = (user input)
    if text is empty break

    if is_palindrome(text)
        print true message
    else
        print false message
    end if

end while
"""

relevant_chars = "abcdefghijklmnopqrstuvwxyz "

def letters(text):
    """Returns the text with non-relevant characters
       stripped. Relevant characters are the letters a-z,
       A-Z and the space character"""

    result = ""
    
    for char in text:
        # Note that while char.lower() is used for
        # comparison, the character with case is appended
        # to the result
        if char.lower() in relevant_chars:
            result += char
    
    return result 

def is_palindrome(text):
    """Determines if the given text is a palindrome.
       Does not ignore case or spaces, but other special
       characters are disregarded."""

    text = letters(text)
    result = True

    for i in range(len(text)//2):
        if text[i] != text[-i-1]:
            result = False

    return result

while True:

    text = input("Enter text: ")

    if text.strip() == "":
        break

    if is_palindrome(text):
        print(text, "is a palindrome.")
    else:
        print(text, "is not a palindrome.")