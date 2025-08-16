# Without passing parameter( without i/p)
# With returning value(with o/p)

def fact():
    n=int(input("Enter a number:"))
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
# res=fact()
# print(f"Factorial is {res}")

print(fact())