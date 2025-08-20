def reverse_number(num, rev=0):
    
    if num == 0:
        return rev
    else:
        digit = num % 10
        
        rev = rev * 10 + digit
   
    return reverse_number(num // 10, rev)

def checkPalindrome(num):
    if num==reverse_number(num):
        print(f"{num} is palindrome number")
    else:
        print(f"{num} is not palindrome number")

n=int(input("Enter a number:"))
checkPalindrome(n)


