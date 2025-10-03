def fun():
    x=20 # x will be different variable...
    print(id(x))
    
x=10
print(id(x))
fun()
print(x)