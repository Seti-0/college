''' (Pseudocode)

Note:
    It isn't specified if the range
    is inclusive or exclusive. I've assumed
    [1, 10000) since that seems to be the python convention

total = 0

for each number in [1,10000):
    if (number % 3 == 0) or (number % 5 == 0):
        add number to total

print(total)

'''

total = 0

for i in range(1, 10000):
    if (i % 3 == 0) or (i % 5 == 0):
        total += i

print(total)