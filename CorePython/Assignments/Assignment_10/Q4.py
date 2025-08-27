# Write a program to reverse the list.

li=[10,20,30,40,50]

rev=[]
print(f'Original list is {li}')
for i in range(len(li),0,-1):
    rev.append(li[i-1])
print(f' Reversed is {rev}')