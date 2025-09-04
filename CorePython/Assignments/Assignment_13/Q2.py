#  Python Program to Concatenate Two Dictionaries Into One

d1 = {1: 11, 2: 12, 3: 13, 4: 14}
d2 = {5: 15, 6: 16, 7: 17, 8: 18}

d3 = d1.copy()   
d3.update(d2)    

print("Concatenated Dictionary:", d3)
