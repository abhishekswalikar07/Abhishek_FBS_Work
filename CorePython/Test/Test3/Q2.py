
N = int(input("Enter the value of N: "))

total_sum = 0
factorial = 1  

for i in range(1, N + 1):
    factorial *= i  
    total_sum += i / factorial

print(f"The sum is: {total_sum}")
