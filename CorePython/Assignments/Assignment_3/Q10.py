#Write a program to check if person is eligible to marry or not (male age >=21 andfemale age>=18)

gender=input("Enter gender(M/F):")
age=int(input("Enter age:"))

if((gender=='M' and age >=21) or (gender=='F' and age >=18)):
    print("Eligible for marriage.")
else:
    print("Not eligible")
