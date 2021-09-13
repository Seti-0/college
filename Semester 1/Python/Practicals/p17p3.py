"""

function count(location: string, target: string)
    index = 0
    count = 0

    (infinite loop)

        (search for target in location, 
            starting at index)

        if search failed then 
            break
        else
            (update index)
            count++
        end if

    (end infinite loop)

    return count
end function

text = (user input)

if count(text, "dog") equals count(text, "cat") then
    (print true)
else
    (print false)
end if
"""

def count(location, target):

    index = 0
    count = 0

    while True:

        index = location.find(target, index)
        
        if index == -1:
            break

        else:
            # Next iteration start searching from
            # after just after the current find
            index += len(target)
            count += 1
    
    return count

text = input("Enter text: ")

cat_count = count(text, "cat")
dog_count = count(text, "dog")

if cat_count == dog_count:
    print("This text satisfies cat dog equality")

elif cat_count > dog_count:
    print("There are more cats than dogs in this text")

elif cat_count < dog_count:
    print("There are more dogs than cats in this text")