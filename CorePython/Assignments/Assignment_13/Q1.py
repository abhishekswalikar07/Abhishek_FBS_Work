#  Python Program to Add a Key-Value Pair to the Dictionary

d={}
n=int(input("Enter how many key-value pair want to add in dicctionary:"))
for i in range(n):
    key=input("Enter key:")
    value=input("Enter value:")

    d[key]=value

print(f"Dictionary is : {d}")