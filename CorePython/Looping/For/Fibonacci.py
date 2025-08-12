n=int(input("Enter number to print n fiboncci number :"))

a,b=-1,1

print(f"First {n} fibonacci numbers are:")
for i in range(n):
    c=a+b
    print(c , end=" ")
    a=b
    b=c
    