"""
while true:

    input = (user input)

    if input <= 0:
        break

    if input >= 366:
        (print error)

    Note to self:
                S    O    N    D    J    F    Mh   Ap   My   Jn   Jl   Au
        days =  30,  31,  30,  31,  31,  28,  31,  30,  31,  30,  31,  31
     offsets =  0,   30,  61,  91,  122, 153, 181, 212, 242, 273, 303, 334, 365

    if input < 31:
        day = input
        month = "September"
        year = "2020"

    elif input < 61:
        day = input - 31
        month = "October"
        year = "2020"

    ...

    elif input < 365:
        day = input - 334
        month = "August"
        year = "2021"

"""
    
# This is a very awkward implementation, and I did not have 
# time to comment it properly.

# I chose not to use lists despite them being by far the
# better choice than what I've just done below because 
# I was unsure if we were allowed to.

while True:

    number = int(input("Enter number: "))

    if number <= 0:
        break

    if number >= 366:
        print("That is not a valid day!")
        # I forgot this "continue" in the previous submission
        continue

    if number < 31:
        day = number
        month = "September"
        year = "2020"

    elif number < 62:
        day = number - 30
        month = "October"
        year = "2020"

    elif number < 92:
        day = number - 30
        month = "November"
        year = "2020"

    elif number < 123:
        day = number - 91
        month = "December"
        year = "2020"

    elif number < 154:
        day = number - 122
        month = "January"
        year = "2021"

    elif number < 182:
        day = number - 153
        month = "Febuary"
        year = "2021"

    elif number < 213:
        day = number - 181
        month = "March"
        year = "2021"

    elif number < 243:
        day = number - 212
        month = "April"
        year = "2021"

    elif number < 274:
        day = number - 242
        month = "May"
        year = "2021"

    elif number < 304:
        day = number - 273
        month = "June"
        year = "2021"

    elif number < 335:
        day = number - 303
        month = "July"
        year = "2021"

    elif number < 366:
        day = number - 334
        month = "August"
        year = "2021"

    print("Day number",str(number),"is",str(day),month,year)

    