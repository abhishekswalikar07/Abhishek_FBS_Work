# WAP to find which numbers are divisible by 7 and multiple of 5 in a given range.

n=int(input("Enter the last number of a range:"))

for i in range(1,n+1):
    if (i%7==0 and i%5==0):
        print(i, end=" ")