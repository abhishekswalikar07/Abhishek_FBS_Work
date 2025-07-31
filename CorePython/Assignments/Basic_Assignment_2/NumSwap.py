# Write a program to swap two numbers using third variable.

x=int(input("Enter first number:"))
y=int(input("Enter second number:"))

print(f' Before swapping: x:{x}, y:{y}')

temp=x
x=y
y=temp

print(f' After swapping: x:{x}, y:{y}')
