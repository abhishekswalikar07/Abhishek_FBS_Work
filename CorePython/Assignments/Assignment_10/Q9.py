# Write a program of having n number of elements in the list and find out even
# and odd elements in that list and then create two separate lists which will have
# even elements and other will have odd elements.

li=[12,43,87,6,89,45,86,57,82]
even=[]
odd=[]

for item in li:
    if item%2==0:
        even.append(item)
    else:
        odd.append(item)
        
print(f'Even numbered list is {even}')
print(f'Odd numbered list is {odd}')