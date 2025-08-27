# Write a program to create a new list from existing list which contains cube of
#each number of list. 

li = [12, 43, 56, 25, 17, 7]

cube = []

for item in li:          
    ele = item ** 3      
    cube.append(ele)

print(f'List of cubes of elements of existing list is {cube}')
