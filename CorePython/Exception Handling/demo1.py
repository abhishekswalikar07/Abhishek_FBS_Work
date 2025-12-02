try:
    n1=int(input("Enter number 1:"))
    n2=int(input("Enter number 2:"))
except:
    print("Invalid input")
else:
    sum=n1+n2
    print(f'Addition of {n1} and {n2} is {sum}')
    