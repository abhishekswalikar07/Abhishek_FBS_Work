num=int(input("Enter number:"))
temp=num
sum = 0
print("Digits are:")
while temp>0:
    d=temp%10
    print(d)
    sum += d
    temp=temp//10
print("Sum of digits:", sum)
