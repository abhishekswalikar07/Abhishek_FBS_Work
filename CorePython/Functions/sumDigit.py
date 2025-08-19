def sumDigit(n):
    if n==0:
        return 0
    else:
        return (n%10)+sumDigit(n//10)
    
num=4567
print("Sum of digit is:",sumDigit(num))