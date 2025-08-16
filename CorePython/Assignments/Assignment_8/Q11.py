
# WAP to check if a given number is Armstrong number or not. 
# For each task create separate functions.

def count_digits(n):
    count = 0
    temp = n
    while temp > 0:
        temp //= 10
        count += 1
    return count

def armstrong_sum(n):
    power = count_digits(n)
    temp = n
    total = 0
    while temp > 0:
        digit = temp % 10
        total += digit ** power
        temp //= 10
    return total


def is_armstrong(n):
    return n == armstrong_sum(n)

num = int(input("Enter a number: "))

if is_armstrong(num):
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")
