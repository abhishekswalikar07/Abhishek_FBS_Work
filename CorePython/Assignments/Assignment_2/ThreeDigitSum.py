# Find the sum of three-digit number.
num=int(input("Enter three digit number:"))
temp=num

d1=temp%10
temp=temp//10

d2=temp%10
temp=temp//10

d3=temp%10
temp=temp//10

sum=d1+d2+d3


print(f'Sum of three digit number is {sum}')

