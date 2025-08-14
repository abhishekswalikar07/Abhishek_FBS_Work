# Write a progrm to print first n prime numbers.

# Print prime numbers upto n
n=int(input("Enter number to print n prime number:"))

count=0
num=2

while(count<n):
    for i in range(2, (num//2)+1):
        if(num%i==0):
            break
            
    else:
        print(num, end=" ")
        count+=1
    num+=1
    
