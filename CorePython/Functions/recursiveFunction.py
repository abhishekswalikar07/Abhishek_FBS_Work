def sos(n):
    if n==0:
        return 0
    else:
        return n+sos(n-1)
    
n=int(input("Enter number:"))
sum=sos(n)
print(sum)