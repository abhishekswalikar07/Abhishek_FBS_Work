# one="Even_odd"
# two="Basic_Salary"

option=int(input("Enter option to choose:"))

if option==1:
    a=int(input("Enter a number:"))
    if a%2==0:
        print(f"{a} ia an even number.")
    else:
        print(f"{a} ia an odd number.")
elif option==2:
    salary=int(input("Enter basic salary:"))
    da=0
    ta=0
    hra=0

    if salary<= 5000 and salary>=0:
        da=(salary*0.1)
        ta=(salary*0.2)
        hra=(salary*0.25)
        total_salary=salary+da+ta+hra
    
    elif salary> 5000:
        da=(salary*0.15)
        ta=(salary*0.25)
        hra=(salary*0.3)
        total_salary=salary+da+ta+hra
    else:
        print(f'{salary} is incorrect.')
    
    print(f"Total salary is {total_salary} Rs")
else:
    print("Enter correct options")
