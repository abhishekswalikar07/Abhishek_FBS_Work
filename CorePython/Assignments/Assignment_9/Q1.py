# Write a program to find sum of following series using recursive functions:

#  1! + 2! + 3! + 4! +..... + n!


def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
    
def sumfact(n):
    if n==0 or n==1:
        return 1
    else:
        return fact(n)+sumfact(n-1)
    
n=int(input("Enter a number:"))
print(f'Sum of series of factorial till {n}! is {sumfact(n)}')