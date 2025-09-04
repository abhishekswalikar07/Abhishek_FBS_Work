# Write a Python program to remove the intersection of a second set with a first set.


A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
c=set()

#1. 
for ele in A:
    if ele not in B:
        c.add(ele)
print("Set A after removing intersection with B:",c)


#2. 
A.difference_update(B)
print("Set A after removing intersection with B:", A)