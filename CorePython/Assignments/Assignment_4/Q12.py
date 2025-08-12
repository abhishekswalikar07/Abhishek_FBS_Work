# WAP to print Armstrong number within a given range


num=int(input("Enter the last number upto which to print armstrong number:"))# 145


for i in range(1, num+1):
    temp=i
    order=0
    while temp>0:
       order+=1
       temp=temp//10
       
    temp=i
    sum_of_powers=0
    
    while temp>0:
        Digit=temp%10
        sum_of_powers+=Digit**order
        temp//=10
    
    if i==sum_of_powers:
        print(i, end=" ")
    