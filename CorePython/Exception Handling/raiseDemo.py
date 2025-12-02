from userException import Userexception

def emp(id,name,age):
    if (not(age>0 and age<121)):
        raise Userexception(age)
    
    print("ID:",id)
    print("NAME:",name)
    print("AGE:",age)

id=int(input("Enter id:"))
name=input("Enter name:")
age=int(input("Enter age:"))
emp(id,name,age)