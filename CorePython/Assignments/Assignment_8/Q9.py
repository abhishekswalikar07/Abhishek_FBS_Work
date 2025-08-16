# Write a program to check if entered number is a palindrome or not.

def checkPalindrome(n):
    temp = n
    rev = 0
    while temp > 0:
        d = temp % 10       
        rev = rev * 10 + d  
        temp //= 10
    if n == rev:
        print(f"{n} is a Palindrome number")
    else:
        print(f"{n} is not a Palindrome number")


num = int(input("Enter number: "))
checkPalindrome(num)

