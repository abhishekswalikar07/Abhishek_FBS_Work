# Write a program to find sum of following series using functions :
# a. 1+ 2 + 3 + 4+..... + n
# b. 1!+ 2! + 3! + 4!+..... + n!
# c. 1^1 + 2^2 + 3^3+ ...... n^n

def sum(n):
    sum=0
    for i in range(n+1):
        sum+=i
    print(f"Sum of the numbers of series upto {n} is {sum}")
    
    
def factSum(n):
    sum=0
    fact=1
    for i in range(1,n+1):
        fact*=i
        sum+=fact
    print(f"Sum of the factorials of numbers of series upto {n} is {sum}")
    


def squareSum(n):
    sum=0
    
    for i in range(1,n+1):
        sum+=i**i
        
    print(f"Sum of the squares of numbers of series upto {n} is {sum}")
    



a=int(input("Enter number:"))
sum(a)
factSum(a)
squareSum(a)



