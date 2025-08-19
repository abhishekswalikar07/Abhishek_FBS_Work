
def evenodd(num):
    if num==0:
        return (f"{num} is neutral")
    elif num % 2==0:
        return (f'{num} is an even number')
    else:
        return (f'{num} is an odd number')

def checkPrime(num):
    for i in range(2, num//2+1):
        if num%i==0:
            return False
    else:
        return True

ch=0
while ch !='4':
    print('''Please select choice from below:
          1. Check even odd
          2. Check positive negative
          3. Prime
          4. Exit''')
    ch=input("Enter choice:")
    
    if ch=='1':
        num=int(input("Enter a number:"))
        res=evenodd(num)
        print(res)
    elif ch=='2':
        pass
    elif ch=='3':
        num=int(input("Enter number:"))
        res=checkPrime(num)
        if res:
            print(f'{num} is a prime number')
        else:
            print(f'{num} is  not a prime number')
    elif ch=='4':
        print("Thank you")
    else:
        print("###  INVALID CHOICE ###")