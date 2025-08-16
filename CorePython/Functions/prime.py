# With passing parameter (with i/p)
#with returning value(with o/p)

def checkPrime(num):
    for i in range(2, num//2+1):
        if num%i==0:
            return False
    else:
        return True
num=int(input("Enter number:"))
res=checkPrime(num)
if res:
    print(f'{num} is a prime number..')
else:
    print(f'{num} is not a prime number')