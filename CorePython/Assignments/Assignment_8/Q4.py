# Sum of all odd numbers between 1 to n

def oddSum(n):
    sum=0
    for i in range(1,n+1):
        if i%2!=0:
            sum+=i
    print(f'Sum of all odd numbers from 1 to {n} is {sum}')
        
a=int(input("Enter last limit number:"))
oddSum(a)