# Write a program to find sum of digits using recursion.

def sumDigit(n):
    if n==0:
        return 0
    else:
        return (n%10)+sumDigit(n//10)
    
num=int(input("Enter a number:"))
print("Sum of digit is:",sumDigit(num))