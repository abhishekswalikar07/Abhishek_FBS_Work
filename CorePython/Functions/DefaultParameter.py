#1. Assigning value to the para/arg in the function definition
#2. Flow should be right to left
#3. Invoking optional parameter concept

def adddition(n1,n2,n3=0,n4=0):
    return n1+n2+n3+n4

print(adddition(10,20,30,40))
print(adddition(34,35))