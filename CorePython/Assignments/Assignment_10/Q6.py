# Write a program to remove duplicates from the list.

li = [10, 20, 10, 30, 20, 40, 50, 40]

li2 = []
for item in li:
    if item not in li2:
        li2.append(item)

print("List after removing duplicates:", li2)
