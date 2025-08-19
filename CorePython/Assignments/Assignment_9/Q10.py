# Write a program to reverse a number using recursion.

def reverse_number(num, rev=0):
    
    if num == 0:
        return rev
    else:
        digit = num % 10
        
        rev = rev * 10 + digit
   
    return reverse_number(num // 10, rev)



n = int(input("Enter a number: "))
res= reverse_number(n)
print(f"Reversed number: {res}")
