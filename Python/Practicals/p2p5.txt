x, y = 0, 5
animals = "herd of elephants"
seg = animals[x:y]
print("Seg: "+seg)
print()

# Q1: What happens if x and y are the same?
# Answer: Nothing.
print("Q1: " + animals[3:3])

# Q2: What happens if x > y
# Answer: Nothing.
print("Q2: " + animals[2:1])

# Q3: What happens if x is omitted?
# Answer: All characters before y are printed.
print("Q3: " + animals[:5])

# Q4: What happens if y is omitted?
# Answer: All characters after x are printed.
print("Q4: " + animals[8:])

# Q5: What happens if x and y are omitted?
# Answer: All characters are printed.
print("Q5: " + animals[:])
