# Create a class Student with following
# a. data members :
# i. StudentId
# ii. Name
# iii. Age
# iv. Percentage
# b. Add the following methods :
# i. Parameterized constructor
# ii. Display
# iii. Accept
# iv. Method CalculateRank
# v. Override __str__ Method


class Student:
    def __init__(self,id=0,nm="",age=0,per=0,grade=""):
        self.id=id
        self.name=nm
        self.age=age
        self.percentage=per
        self.grade=grade
    
    def Accept(self):
        self.id=int(input("Enter Student Id:"))
        self.name=input("Enter Student Name:")
        self.age=int(input("Enter student age:"))
        a=int(input("Enter First subject marks:"))
        b=int(input("Enter second subject marks:"))
        c=int(input("Enter third subject marks:"))
        if 0<=a<=100 and 0<=b<=100 and 0<=c<=100:
            self.total=a+b+c
            self.percentage=(self.total/3)

    def DisplayData(self):
        print("Student ID:",self.id)
        print("Student Name:",self.name)
        print("Student Age:",self.age)
        print("Student Percentage:",self.percentage)

    
    def CalculateRank(self):
        if self.percentage>90:
            self.grade="A+"
        elif self.percentage>80 and self.percentage<=90:
            self.grade="A"
        elif self.percentage>70 and self.percentage<=80:
            self.grade="B"
        elif self.percentage>60 and self.percentage<=70:
            self.grade="C"
        elif self.percentage>50 and self.percentage<=60:
            self.grade="D"
        elif self.percentage>=40 and self.percentage<=50:
            self.grade="E"
        elif self.percentage>=0 and self.percentage<40:
            self.grade="Fail"
        else:
            print("Enter correct percentage...")
        print("Percentage Grade is:",self.grade)

    def __str__(self):
        return (f"Student :[ID={self.id}, Name={self.name}, Age={self.age}, "
                f"Percentage={self.percentage}, Grade={self.grade}]")
        
    
# s1=Student()
# s1.Accept()
# s1.DisplayData()
# s1.CalculateRank()
# print(s1)