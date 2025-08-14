# Write a program to input angles of a triangle and check whether triangle is valid or not.

a=int(input("Enter first angle of triangle:"))
b=int(input("Enter first angle of triangle:"))
c=int(input("Enter first angle of triangle:"))

D=a+b+c

if D==180:
    print("Triangle is valid.")
else:
    print("Triangle is invalid.")