"""

(start infinite loop)

    text = (user input)

    if (text is empty) then

        (exit loop)

    end if

    count = 0

    for i from 0 to (length of text) do
        
        if ((letter i of text) is a vowel) then

            count++

        end if

    end for

    (print count)

(end infinite loop)


"""

# To check if a character is a vowel, check
# if this list contains it
vowels = ['a', 'u', 'o', 'i', 'e']

while True:

    # Promt the user for input. Take the lower
    # case of the input to simplify vowel detection
    text = input("Enter text: ").lower()

    # Exit condition
    if text == "":
        break

    count = 0
    for i in range(len(text)):
        if text[i] in vowels:
            count += 1

    print(f"There are {count} vowels in that text.")
    