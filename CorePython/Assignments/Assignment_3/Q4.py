# Write a program to input all sides of a triangle and check whether triangle is valid or not.

a=int(input("Enter first side of triangle:"))
b=int(input("Enter second side of triangle:"))
c=int(input("Enter third side of triangle:"))

if a+b>c and b+c>a and a+c>b:
    print("Triangle is valid")
else:
    print("Triangle is invalid.")