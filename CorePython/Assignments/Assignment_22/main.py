# 1.Create a class Emp (eid,ename,basic)
# 2. WAP a menu driven program to perform following operations using
# files :

# a. Add a record
# b. Search for a record using id
# c. Delete a record using id
# d. Edit a record using id.
# e. Display all records.

from EmpManage import EmpManage
def login():
    userid='admin'
    passw='1234'

    user=input("Enter username: ")
    password=input("Enter password:")

    if user==userid and password==passw:
        print("Logged in successfully...")

        ch=0
        while ch!='6':
            print("""Please choose option from below:
                1. Add employee record
                2. Search employee
                3. Delete Employee record
                4.Update employee record
                5. Display all record
                6. Exit""")
            ch=input("Enter option:")
            if ch=='1':
                EmpManage.addEmp()
            elif ch=='2':
                EmpManage.searchEmp()
            elif ch=='3':
                EmpManage.delEmp()
            elif ch=='4':
                EmpManage.updEmp()
            elif ch=='5':
                EmpManage.DisplayEmp()
            elif ch=='6':
                print("Thank you... ")
            else:
                print("Invalid choice..")
    else:
        print("Invalid credentials...")
    

ch=0
while ch !='2':
    print("""Please choose option from following:
          1. Login
          2.Exit""")
    ch=input("Enter choice:")
    if ch=='1':
        login()
    elif ch=='2':
        print("Thank you...")
    else:
        print("Invalid options...")


