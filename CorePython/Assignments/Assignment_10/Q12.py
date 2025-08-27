# Write a program to create three lists of numbers, their squares and cubes

li=[3,6,2,8,9,4,7]
square=[]
cube=[]

for ele in li:
    m=ele**2
    square.append(m)
    n=ele**3
    cube.append(n)
    
print(f'Original list: {li}')
print(f'List of squares of elements  Original list: {square}')
print(f'List of cubes of elements  Original list: {cube}')