a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=0

op=input("Enter which operation to perform(+,-,*,/,%):")

if op=="+":
   c=a+b
   print(f"{a}+{b}={c}") 
elif op=="-":
   c=a-b
   print(f"{a}-{b}={c}") 
elif op=="*":
   c=a*b
   print(f"{a}*{b}={c}") 
elif op=="/":
   c=a/b
   print(f"{a}/{b}={c}") 
elif op=="%":
   c=a%b
   print(f"{a}%{b}={c}") 
else:
    print("Numbers are not corrcet")