# WAP to print sum of series upto n.


n = int(input("Enter a positive integer: "))

total = 0 

for i in range(1, n + 1):
    total += i  

print(f"The sum of the series up to {n} is: {total}")
