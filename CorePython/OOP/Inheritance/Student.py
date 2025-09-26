from Person import Person
class Student(Person):
    def __init__(self, nm, age, add,rollno,course,):
        super().__init__(nm, age, add)
        self.rollno=rollno
        self.course=course
    def displayData(self):
        super().displayData()
        print("Roll No:",self.rollno)
        print("Course:",self.course)
    

s1=Student("Abhi",23,"Sangli",101,"Python")
s1.displayData()
