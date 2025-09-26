# Create a class College which has collection of students. Add the
# following methods :
# a. Parameteried constructor for number of students.
# b. AddStudent
# c. GetStudent
# d. RemoveStudent
# e. Override __str__ Method

from Q1 import Student   # Import Student class

class College:
    def __init__(self, capacity=0):
        """Constructor with max number of students"""
        self.capacity = capacity
        self.students = []

    # Add student interactively
    def AddStudent(self):
        if len(self.students) >= self.capacity:
            print("College capacity full! Cannot add more students.")
            return
        student = Student()
        student.Accept()        # Input student details
        student.CalculateRank() # Calculate grade
        self.students.append(student)
        print(f"Student {student.name} added successfully.\n")

    # Get student interactively
    def GetStudent(self):
        if not self.students:
            print("No students in college.")
            return
        student_id = int(input("Enter Student ID to fetch: "))
        for s in self.students:
            if s.id == student_id:
                print("Student Found:")
                s.DisplayData()
                return
        print(f"Student with ID {student_id} not found.")

    # Remove student interactively (without try-except)
    def RemoveStudent(self):
        if not self.students:
            print("No students in college.")
            return
        student_id = int(input("Enter Student ID to remove: "))
        for s in self.students:
            if s.id == student_id:
                self.students.remove(s)
                print(f"Student {s.name} removed successfully.")
                return
        print(f"Student with ID {student_id} not found.")

    # Display all students
    def __str__(self):
        if not self.students:
            return f"College(capacity={self.capacity}, No Students)"
        student_details = "\n".join(str(s) for s in self.students)
        return f"College(capacity={self.capacity}, Students:\n{student_details})"


# Example usage
if __name__ == "__main__":
    c1 = College(3)  # College with max 3 students

    while True:
        print("\n--- College Menu ---")
        print("1. Add Student")
        print("2. Get Student by ID")
        print("3. Remove Student by ID")
        print("4. Show All Students")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            c1.AddStudent()
        elif choice == '2':
            c1.GetStudent()
        elif choice == '3':
            c1.RemoveStudent()
        elif choice == '4':
            print(c1)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")
