# Write a program to accept 3 digit number. If first digit is double of second digit and half of
# third digit then display “Yes, you have done it”, otherwise display “Please try next time”.

Num=int(input("Enter three digit number:")) # 214

temp=Num

d1=temp%10 # 4
temp=temp//10 # 21

d2=temp%10 # 1
temp=temp//10 #2

d3=temp%10  #2
temp=temp//10  #0

if d3 //d2==2 and d3*2==d1 :
    print(f'{Num} is correct.. You have done it.')
else:
    print("Please try next time..")
        
        