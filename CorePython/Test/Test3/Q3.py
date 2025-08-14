n=int(input("Enter total number of employees: "))
temp=n
total_emp_salary=0
for i in range(1,n+1):
    salary=int(input(f"Enter basic salary of employee {i}:"))
    
    if salary <=20000:
        da=salary*0.1
        ta=salary*0.12
        hra=salary*0.15
        total_salary=salary+da+ta+hra
        print(f'Total salary of employee {i} is {total_salary}')
    elif salary>20000:
         da=salary*0.15
         ta=salary*0.18
         hra=salary*0.2
         total_salary=salary+da+ta+hra
         print(f'Total salary of employee {i} is {total_salary}')
    total_emp_salary+=total_salary  
print(f"Total salary of {n} employees is {total_emp_salary}")