# Q2: Missing coin without using inbuilt functions

n = int(input("Enter original number of coins: "))

coins = []
print("Enter the coin numbers:")
for i in range(n - 1):       
    num = int(input())
    coins.append(num)

missing = 0
for i in range(len(coins)):
    missing = missing ^ coins[i]   # XOR cancels even numbers, leaves missing one

print("The missing coin number is:", missing)