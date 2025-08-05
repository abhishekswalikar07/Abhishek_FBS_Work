a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))

if a>0 and b>0 and c>0:  
    if a>b:
        if a>c:
            print(f'{a} is greater than {b,c}')
        else:
            print(f'{c} is greater than {a,b}')
    else:
        if b>c:
            print(f'{b} is greater than {a,c}')  
        else:
            print(f'{c} is greater than {a,b}')      
else:
    print("Numbers are incorrect.")