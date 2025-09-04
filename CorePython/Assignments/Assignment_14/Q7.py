# Given two sets of numbers, write a Python program to find the missing
# numbers in the second set as compared to the first and vice versa.
# Use the Python set.

a={10,22,45,34,54}
b={22,45,34,10,67}

#1.
print("Set of missing numbers compared to each other in both set:",a.symmetric_difference(b))

#2.

for ele in a:
    if ele not in b:
        print(f'{ele} is not present in set {b}')
for ele in b:
    if ele not in a:
        print(f'{ele} is not present in set {a}')
