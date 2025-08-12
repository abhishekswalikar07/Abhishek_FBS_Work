# Write a program to check if given number is Armstrong number or not.

num = int(input("Enter a number: "))

original_num = num
sum_of_powers = 0

digits = 0
temp = num
while temp > 0:
    digits += 1
    temp //= 10

temp = num
while temp > 0:
    digit = temp % 10
    sum_of_powers += digit ** digits
    temp //= 10

if sum_of_powers == original_num:
    print(f"{original_num} is an Armstrong number.")
else:
    print(f"{original_num} is not an Armstrong number.")
