gender=input("Enter gender(M/F):")
age=int(input("Enter age:"))

if((gender=='M' and age >=21) or (gender=='F' and age >=18)):
    print("Eligible for marriage.")
else:
    print("Not eligible")
