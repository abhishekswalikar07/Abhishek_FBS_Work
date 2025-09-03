# 9. Write a program to create three lists of numbers, their squares and cubes

def tree_list(num):
    li = [i for i in range (1,n+1)]
    squre_li = [i**2 for i in range (1,n+1)]
    cube_li = [i**3 for i in range (1,n+1)]
    print(f'''lists of numbers: {li}
lists of squares: {squre_li}
lists of cubes: {cube_li}''')

n = int(input("Enter the number: "))
tree_list(n)