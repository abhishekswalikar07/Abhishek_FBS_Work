# WAP to calculate total salary of employee based on basic, da=10% of basic,ta=12% of basic, hra=15% of basic.

Basic_Salary=float(input("Enter basic salary:"))
print(f'Basic salary:{Basic_Salary}')

da=Basic_Salary*0.1
ta=Basic_Salary*0.12
hra=Basic_Salary*0.15

Total_Salary=Basic_Salary+da+ta+hra

print(f'Total salary of employee is: {Total_Salary}')

