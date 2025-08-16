#  Write a program to find sum of digits of a number.

def digitSum(n):
    temp = n
    sum = 0
    while temp > 0:       
        d = temp % 10
        sum += d
        temp = temp // 10
    print("Sum of digits:", sum)

num = int(input("Enter number: "))
digitSum(num)
