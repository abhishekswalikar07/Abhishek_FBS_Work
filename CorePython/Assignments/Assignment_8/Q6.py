# Write a program to find print the following Fibonacci series using
# functions:
# 1 1 2 3 5 8 n terms

def fibo(n):
    a,b=1,0
    c=0
    print(f"fibonacci series upto first {n} numbers is :")
    for i in range(1,n+1):
        c=a+b
        print(c, end=" ")
        a=b
        b=c
    

a=int(input("Enter number:"))
fibo(a)