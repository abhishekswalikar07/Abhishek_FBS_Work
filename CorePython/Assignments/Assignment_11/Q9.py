# 9. Write a program to create three lists of numbers, their squares and cubes

def tree_list(n):
    
    numbers = []
    for i in range(1, n + 1):
        numbers.append(i)

    squares = []
    for i in range(1, n + 1):
        squares.append(i ** 2)

    cubes = []
    for i in range(1, n + 1):
        cubes.append(i ** 3)
   
    print("List of numbers:", numbers)
    print("List of squares:", squares)
    print("List of cubes:", cubes)

n = int(input("Enter the number: "))
tree_list(n)