from empManage import Emp

def login():
    userid="user"
    password="1234"
    attempts=3
    uname=input("Enter user id:")
    passw=input("Enter password:")

    if uname==userid and passw==password:
       print("Logged in succcessfully...")

       ch=0
       while ch!="6":
           print("""Please select option from below:
                 1. Add employee
                 2. Update employee
                 3. Remove Employee 
                 4. Show All employee 
                 5. Search employee
                 6. Exit """)
           ch=input("Enter choice:")

           if ch=="1":
               Emp.addEmp()
           elif ch=="2":
               Emp.updEmp()     
           elif ch=="3":
               Emp.delEmp()
           elif ch=="4":
               Emp.showAllEmp()
           elif ch=="5":
               Emp.searchEmp()
           elif ch=="6":
               print("Thank you...")
           else:
            print("Invalid Choice!!!")
    else:
        attempts-=1
        print("Invalid credentials...")


ch=0
while ch!='2':
    print(''' Please select option from below:
          1.Login
          2.Exit''')
    ch=input("Enter choice:")

    if ch=="1":
        login()
    elif ch=="2":
        print("Thank you...")
    else:
        print("Invalid choice...")