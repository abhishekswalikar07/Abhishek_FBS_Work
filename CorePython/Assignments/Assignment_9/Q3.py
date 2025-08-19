# Write a program to reverse a given number using recursive function.

def reverse_number(num, rev=0):
    
    if num == 0:
        return rev
    else:
        digit = num % 10
        
        rev = rev * 10 + digit
   
    return reverse_number(num // 10, rev)



n = int(input("Enter a number: "))
result = reverse_number(n)
print(f"Reversed number: {result}")
