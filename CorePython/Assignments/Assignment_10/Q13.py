# Write a program to print list after removing even numbers.

li=[23,45,24,56,76,87,96,33,75]
odd=[]
print(f'Original list is: {li}')
for item in li:
    if item%2!=0:
        odd.append(item)
print(f'List after removing even numbers from originallist is: {odd}')