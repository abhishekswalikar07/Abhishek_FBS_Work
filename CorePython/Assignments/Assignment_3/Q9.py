m1=int(input("Enter first subject marks:"))
m2=int(input("Enter second subject marks:"))
m3=int(input("Enter third subject marks:"))
m4=int(input("Enter fourth subject marks:"))
m5=int(input("Enter fifth subject marks:"))

total_marks=m1+m2+m3+m4+m5

per=(total_marks / 500) * 100

if per>=75:
    print("Grade is First class.")
elif per>=65 and per<75:
    print("Grade is second class.")
elif per>=55 and per<65:
    print("Grade is third class.")
elif per>=55 and per<65:
    print("Grade is fourth class.")
elif per>=45 and per<55:
    print("Grade is Fifth class.")
elif per>=35 and per<45:
    print("Grade is Pass.")
else:
    print("Grade is Fail.")