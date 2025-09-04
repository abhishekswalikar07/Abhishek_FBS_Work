#  Python Program to Generate a Dictionary that Contains Numbers (between 1
# and n) in the Form (x,x*x).

d={}
n=int(input("Enter how many keys-value pair you want to add in dictionary:"))

for i in range(1,n+1):
    key=int(input("Enter key number:"))
    value=key*key
    
    d[key]=value
print("Dictionary is", d)
    

