# Use a nested list comprehension to find all of the numbers from
# 1–1000 that are divisible by any single digit.

li = [x for x in range(1, 1001) if  [y for y in range(2, 10) if x % y == 0]]
print(li)

# li = [x for x in range(1, 1001) if all(x % y == 0 for y in range(2, 10))]
# print("Numbers divisible by 2–9:", li)





