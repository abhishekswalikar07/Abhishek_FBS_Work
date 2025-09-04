#  Python Program to Multiply All the Items in a Dictionary

d = {1: 11, 2: 12, 3: 13, 4: 14, 5: 15}
total = 1

for value in d.values():   
    total *= value

print("Sum of all items in dictionary:", total)
