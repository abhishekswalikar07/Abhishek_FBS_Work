# Write a program to check if given number is Armstrong or not using recursive
#  function.

def digit(n):
    if n==0:
        return 0
    else:
        return 1 + digit(n//10)
    
def checkArmstrong(num, temp=None, power=None):
    
    if temp is None:
        temp = num
    if power is None:
        power = digit(num)

   
    if num == 0:
        return 0

    digits = num % 10
    return (digits ** power) + checkArmstrong(num // 10, temp, power)
    
n = int(input("Enter a number: "))

if checkArmstrong(n) == n:
    print(f"{n} is an Armstrong number.")
else:
    print(f"{n} is not an Armstrong number.")