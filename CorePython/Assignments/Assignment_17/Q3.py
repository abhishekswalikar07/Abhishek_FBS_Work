# Create a class MedicalStudent inherited from Student with following :

# i. Data members :Specialization
# ii. MarksOfInternship
# b. Add the following methods :
# i. Parameterized constructor
# ii. Display
# iii. Accept
# iv. override Method CalculateRank
# v. Override __str__ Method


from Q1 import Student


class MedicalStudent(Student):
    def __init__(self, id=0, nm="", age=0, per=0, grade="",specialization="",MarksOfInternship=0):
        super().__init__(id, nm, age, per, grade)
        self.special=specialization
        self.IntMarks=MarksOfInternship
    
    def Accept(self):
        super().Accept()
        self.special=input("Enter Specialisation:")
        self.IntMarks=int(input("Enter Internship Marks:"))

    def DisplayData(self):
        super().DisplayData()
        print("Specialization:",self.special)
        print("Marks of Internship:",self.IntMarks)
    
    def CalculateRank(self):
        super().CalculateRank()
        if 0<=self.IntMarks<=100:
            self.TotalMarks=(self.total+self.IntMarks)/4
        else:
            print("Invalid Internal marks...")
            return
        # print(self.TotalMarks)

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
        print("Total grade including Subject Marks and Internship  Marks is:",self.grade)

    def __str__(self):
        return (super().__str__()[:-1] +   
                f", Specialization={self.special}, InternshipMarks={self.IntMarks}, "
                f"FinalMarks={self.TotalMarks}]")


s1=MedicalStudent()
s1.Accept()
s1.DisplayData()
s1.CalculateRank()
print(s1)

