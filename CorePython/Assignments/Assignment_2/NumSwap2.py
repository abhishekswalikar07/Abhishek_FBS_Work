# Write a program to swap two numbers without using third variable.

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))

print(f' Before swapping a:{a}, b:{b}')
a=a+b   # a=10+20=30
b=a-b   # b=30-20=10 
a=a-b   # a=30-10=20

print(f' After swapping: a:{a}, b:{b}')