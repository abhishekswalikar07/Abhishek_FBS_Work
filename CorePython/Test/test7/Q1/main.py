from bookManage import BookManage
def login():
    userid='user'
    passw='1234'
    attempts=3
    uname=input("Enter user id:")
    password=input("Enter password:")

    if uname==userid and password==passw:
       print("Logged in succcessfully...")

       ch=0
       while ch!="5":
           print("""Please select option from below:
                 1. Add books
                 2. Delete book
                 3. Show All books 
                 4. Search book
                 5. Exit """)
           ch=input("Enter choice:")

           if ch=="1":
               BookManage.addBook()
           elif ch=="2":
               BookManage.delBook()    
           elif ch=="3":
               BookManage.showBook()
           elif ch=="4":
               BookManage.searchBook()
           elif ch=="5":
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