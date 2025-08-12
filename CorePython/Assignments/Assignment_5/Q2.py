# Enter number of students from user. For those many students accept marks of 5
# subject marks from user and calculate percentage. Display all percentage and
# average percentage of students.


num_students = int(input("Enter number of students: "))

total_percentage_sum = 0  

for i in range(1, num_students + 1):
    print(f"\nEnter marks for Student {i}:")
    total_marks = 0

    for j in range(1, 6):
        marks = float(input(f"  Enter marks for subject {j}: "))
        total_marks += marks
    
    percentage = (total_marks / 500) * 100
    total_percentage_sum += percentage
    
    print(f"Percentage of Student {i}: {percentage:.2f}%")

average_percentage = total_percentage_sum / num_students
print(f"\nAverage Percentage of all students: {average_percentage:.2f}%")
