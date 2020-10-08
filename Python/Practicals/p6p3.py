''' (Pseudocode)

name = (user input)

if name is Kieran:
    print "that is a cool name!"

else if (name is "Mickey Mouse" 
        or name is "Sponge..."):
    print "are you sure?"

else print: "you have a nice name"

'''

# (I have purposely ommited any robustness
# for fear of stepping into territory we're not
# meant to be in)

name = input("What is your name: ")

if name == "Kieran":
    print("That is a cool name!")

elif name == "Spongebob Squarepants" or name == "Mickey Mouse":
    print("Are you sure that is your name?")

else:
    print("You have a nice name")

