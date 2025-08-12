# Write a program to print prime numbers between 1 to 100.

print("prime number from 1 to 100:")

count=0
num=2

for i in range(99):
    for i in range(2, (num//2)+1):
        if(num%i==0):
            break
            
    else:
        print(num, end=" ")
        count+=1
    num+=1