
"""
function is_palindrome(text)
    letters = letters_only(text)

    result = True 

    for i from 0 to length of letters
        if letters[i] != letters[length - i]
            result = False
            break
        end if
    end for

    (return result)
end function

function letters_only(text)

    letters = (empty string)

    for each character in text,
        if it is a letter,
            append it to letters
        end if
    end for

    return letters
end function

while true

    text = (user input)

    if text is empty, break

    (use is_palindrome)

end while
"""

def letters_only(text):
    """Returns the text in lower case and stripped of characters
        outside the English alphabet."""

    letters = ""

    for char in text.lower():
        if char in "abcdefghijklmnopqrstuvwxyz":
            letters += char

    return letters

def is_palindrome(text):
    """Returns true if the text is a palindrome, else false. Ignores
       case and characters that are not in the English alphabet."""

    letters = letters_only(text)
    midpoint = len(letters)//2

    result = True

    for i in range(0, midpoint):
        if letters[i] != letters[-i-1]:
            result = False
            break

    return result


while True:

    text = input("Enter text: ")

    if text.strip() == "":
        print("Exiting program")
        break

    if is_palindrome(text):
        print("This is a palindrome")
    else:
        print("This is not a palindrome")
