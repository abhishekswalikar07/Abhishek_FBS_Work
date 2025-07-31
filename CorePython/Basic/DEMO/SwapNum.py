# TO SWAP TWO NUMBERS
# 1. USING THIRD VARIABLE

x=int(input("Enter first number:"))
y=int(input("Enter second number:"))

print(f' Before swapping: x:{x}, y:{y}')

temp=x
x=y
y=temp

print(f' After swapping: x:{x}, y:{y}')


#2. WITHOUT USING THIRD VARIABLE

a=int(input("Enter third number:"))
b=int(input("Enter fourth number:"))

print(f' Before swapping a:{a}, b:{b}')
a=a+b #30
b=a-b #10
a=a-b

print(f' After swapping: a:{a}, b:{b}')

m=10 
n=20
m,n=n,m
print(m,n)