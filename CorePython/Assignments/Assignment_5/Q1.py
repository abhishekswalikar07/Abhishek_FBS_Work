# Write a program to prompt user to enter userid and password. If Id and
# password is incorrect give him chance to re-enter the credentials. Let him try 3
# times. After that program to terminate.


id=123
pwd=12345

for attempgt in range(1,4):
    userid=int(input("Enter user ID:"))
    password=int(input("Enter password:"))
    
    if userid==id and password==pwd:
        print("Login successfully.") 
        break
        
    else:
        print("Invalid credentials. Try again")

else:
    print("Too many attempts. Try again later!!!")