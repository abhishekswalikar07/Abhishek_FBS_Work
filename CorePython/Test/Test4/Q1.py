def factor(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            print(i, end=" ")
        count+=1
            
n=int(input("Enter a number:"))
print(f'Factors of {n}: ', end=" ")
factor(n)
