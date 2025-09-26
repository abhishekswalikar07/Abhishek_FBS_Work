# Create a derived class from Student as EnggStudent with :
# a. Data members as :
# i. Branch
# ii. InternalMarks
# b. Add the following methods :
# i. Parameterized constructor
# ii. Display
# iii. Accept
# iv. override Method CalculateRank
# v. Override __str__ Method


from Q1 import Student

class EnggStudent(Student):
    def __init__(self, id=0, nm="", age=0, per=0, grade="", branch="", InternalMarks=0):
        super().__init__(id, nm, age, per, grade)
        self.branch=branch
        self.internalMarks=InternalMarks

    def Accept(self):
        super().Accept()
        self.branch=input("Enter branch Name:")
        self.internalMarks=int(input("Enter internal marks:"))
        
    
    def DisplayData(self):
        super().DisplayData()
        print("Branch:",self.branch)
        print("Internal Marks:",self.internalMarks)

    

    def CalculateRank(self):
        super().CalculateRank()
        if 0<=self.internalMarks<=100:
            self.TotalMarks=((self.internalMarks+self.total)/2)
        
        if self.TotalMarks>90:
            self.grade="A+"
        elif self.TotalMarks>80 and self.TotalMarks<=90:
            self.grade="A"
        elif self.TotalMarks>70 and self.TotalMarks<=80:
            self.grade="B"
        elif self.TotalMarks>60 and self.TotalMarks<=70:
            self.grade="C"
        elif self.TotalMarks>50 and self.TotalMarks<=60:
            self.grade="D"
        elif self.TotalMarks>=40 and self.TotalMarks<=50:
            self.grade="E"
        elif self.TotalMarks>=0 and self.TotalMarks<40:
            self.grade="Fail"
        else:
            print("Enter correct percentage...")
        print("Total grade including Subject Marks and Internal Marks is:",self.grade)
    
    # def __str__(self):
    #     return super().__str__()[:-1] + f", Branch={self.branch}, InternalMarks={self.internalMarks}]"
    
    def __str__(self):
        return (f"EnggStudent[ID={self.id}, Name={self.name}, Age={self.age}, "
            f"Branch={self.branch}, InternalMarks={self.internalMarks}, "
            f"Percentage={self.percentage}, Grade={self.grade}]")



s1=EnggStudent()
s1.Accept()
s1.DisplayData()
s1.CalculateRank()
print(s1)



    