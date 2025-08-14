
#Write a program to calculate the percentage of student based on marks of any 5 subjects.

m1=int(input("Enter first subject marks:"))
m2=int(input("Enter second subject marks:"))
m3=int(input("Enter third subject marks:"))
m4=int(input("Enter fourth subject marks:"))
m5=int(input("Enter fifth subject marks:"))

total_marks=m1+m2+m3+m4+m5

per=(total_marks / 500) * 100
print(f'Percentage of  marks is {per}%')