# Write a program to print Fibonacci series using recursion.

def fibo(n,a,b):
    if n>0:
        c=a+b
        print(c, end=" ")
        fibo(n-1,b,c)
        
num=int(input("Enter number:"))
a=-1
b=1
fibo(num,a,b,)