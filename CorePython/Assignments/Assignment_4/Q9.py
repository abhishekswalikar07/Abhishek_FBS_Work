# WAP to print all numbers in a range divisible by a given number.

n=int(input("Enter a number:"))

limit=int(input("Enter the last number of a range:"))

print(f'Numbers till {limit} which are divisible by {n} are :')
for i in range(1, limit+1):
    if i%n==0:
        print(i, end=" ")
