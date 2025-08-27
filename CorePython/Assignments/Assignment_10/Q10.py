# Write a program to remove all occurrences of a given element in the list.

li = [12, 43, 56, 43, 27, 67, 43]

ele = int(input("Enter element to remove: "))

new_list = []     

for item in li:
    if item != ele:     
        new_list.append(item)

print("Original List:", li)
print(f"List after removing all occurrences of {ele}:", new_list)


