def add(x,y):
    return x+y

def fact(n):
    f=1
    for i in range(1,n+1):
        f*=i
    return f
def chkEven(n):
    return n%2==0

if __name__=="__main__":
    print(add(10,20))
    print(fact(5))
    print(chkEven(24))
