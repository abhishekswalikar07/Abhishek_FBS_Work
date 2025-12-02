# Write a program to
# 1. create a package “SY” which has class SYMARKS (Computer Total,
# MathsTotal, ElectronicsTotal).
# 2. Create another package “TY” which has a class TYMarks (Theory,
# Practical).
# 3. Create object of student class (Outside SY & TY package) having roll
# number, name, SYMakrs and TYMarks. Add the marksof SY and TY
# Computer subjects and calculate grade ("A" for >=70, "B" for >=60,
# "C" for >=50, “Pass Class” for >=40 else “Fail”) and display the result
# of the student in proper format.


from TY.TYMARKS import TYMARKS

class Student(TYMARKS):

    def __init__(self, CSTotal, MathTotal, ElecTotal, Theory, Practical,name,rollno):
        super().__init__(CSTotal, MathTotal, ElecTotal, Theory, Practical)
        self.name=name
        self.roll=rollno
        self.per=0
        self.grade=""
    
    def TotalMarks(self):
        super().TotalMarks()
        self.per=self.Total/5
        if self.per>=70:
            self.grade="A"
        elif self.per>=60 and self.per<70:
            self.grade="B"
        elif self.per>=50 and self.per<60:
            self.grade="C"
        elif self.per>=40 and self.per<50:
            self.grade="D"
        elif self.per>=0 and self.per<40:
            self.grade="Fail"
        else:
            print("Invalid marks...")
    
    def showDetails(self):
        print("\n----------- Student Result -----------")
        print(f"Roll No: {self.roll}")
        print(f"Name   : {self.name}")
        print("SY Marks:")
        print(f"  Computer     : {self.cs}")
        print(f"  Maths        : {self.math}")
        print(f"  Electronics  : {self.elec}")
        print("TY Marks:")
        print(f"  Theory       : {self.theory}")
        print(f"  Practical    : {self.practical}")
        print("--------------------------------------")
        print(f"Total Marks : {self.Total}")
        print(f"Percentage: {self.per}")
        print(f"Grade: {self.grade}")
        print("--------------------------------------")


name=input("Enter student name:")
roll=int(input("Enter roll number:"))
print("\nEnter SY marks:")
cs=int(input("Enter cs marks:"))
maths=int(input("Enter maths marks:"))
elec=int(input("Enter electronics marks:"))

print("\nEnter TY Marks:")
theory = int(input("Theory: "))
practical = int(input("Practical: "))

student=Student(cs,maths,elec,theory,practical,name,roll)
student.TotalMarks()
student.showDetails()