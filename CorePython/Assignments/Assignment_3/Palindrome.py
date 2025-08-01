# Write a program to reverse three-digit number.
num=int(input("Enter three digit number:")) #258
temp=num #258

d1=temp%10 # 8
temp=temp//10 # 25

d2=temp%10 #5
temp=temp//10 #2

d3=temp%10 # 2  
temp=temp//10 # 0

reverse_num=d1*100+d2*10+d3

if reverse_num == num:
    print(f'{num} is palindrome number.')
# print(f'Reverse of {num} is {reverse_num}')