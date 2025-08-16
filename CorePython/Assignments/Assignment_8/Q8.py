# Write a program find reverse of a number

def reverseNumber(n):
    temp = n
    rev = 0
    while temp > 0:
        d = temp % 10       
        rev = rev * 10 + d  
        temp = temp // 10   
    print(f"Reverse of {n} is {rev}")

num = int(input("Enter number: "))
reverseNumber(num)
