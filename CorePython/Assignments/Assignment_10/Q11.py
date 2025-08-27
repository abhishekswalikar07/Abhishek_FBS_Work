# Write a program to print all numbers which are divisible by m and n in the list.

li=[12,56,24,60,56,35,48,87,84,62]

m=int(input("Enter a number:"))
n=int(input("Enter second number:"))
print(f'Numbers which are divisible by {m} and {n} from list {li} is:')
for ele in li:
    if ele%m==0 and ele%n==0:
        print(ele, end=" ")
