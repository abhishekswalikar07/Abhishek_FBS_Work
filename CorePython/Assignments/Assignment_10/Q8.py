#Write a program to create a duplicate of an existing list. It should not point to
#same list.

li = [12, 43, 56, 84, 47]
dup = []

for item in li:
    dup.append(item)   

print("Original list:", li)
print("Duplicate list:", dup)
print("Are both lists same object?", li is dup) 

