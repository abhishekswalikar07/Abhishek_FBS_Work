# Write a program to find maximum and minimum element in a list.

li=[10,30,50,40,20]

max=li[0]
min=li[0]
for i in range(1,len(li)):
    if li[i]>max:
        max=li[i]
print("Maximum number is:",max)

for i in range(1,len(li)):
    if li[i]<min:
        min=li[i]
print("minimum number is:",min)