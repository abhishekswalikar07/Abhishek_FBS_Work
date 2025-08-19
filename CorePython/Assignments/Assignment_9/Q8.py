# Write a program to check whether a number is prime or not using recursion.

def isPrime(n, i=2):
    if n <= 1:
        return False
    if i == n:  
        return True
    if n % i == 0:
        return False
    return isPrime(n, i+1)


num = int(input("Enter a number: "))
if isPrime(num):
    print(num, "is Prime")
else:
    print(num, "is Not Prime")

    
    
        