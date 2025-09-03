emp = {}

ch = 0
while(ch != '6'):
    print('''Please select option from below:
    1. Add employee
    2. Update employee
    3. Delete employee
    4. Search employee
    5. Show all employees
    6. Exit
    ''')
    ch = input("Enter choice:")
    if(ch == '1'):
        id = input("Enter eid:")
        name = input("Enter ename:")
        sal = float(input("Enter salary:"))
        # eData = ', '.join([id, name, sal])
        eData = f'{id}, {name}, {sal}'
        emp[id] = eData
        print("Employee added successfully....")
    elif(ch == '2'):
        id = input("Enter id from updating employee detail:")
        if(id in emp.keys()):
            eData = emp[id]
            eList = eData.split(', ')
            # print(eList)
            chk = input("Do you want to change name(y/n):") #Y, y, Yes, YES, yES, yes
            if(chk.lower() in ['y', 'yes']):
                eList[1] = input("Enter new name:")
            chk = input("Do you want to change salary(y/n):")
            if(chk.lower() in ['y', 'yes']):
                eList[2] = input("Enter new salary:")
            eData = ', '.join(eList)
            emp[id] = eData
            print("Data updated successfully....")
        else:
            print("Employee id not found.")
            
    elif(ch == '3'):
        pass
    elif(ch == '4'):
        pass
    elif(ch == '5'):
        print(emp)
    elif(ch == '6'):
        print("Thank you for choosing us!")
    else:
        print("Invalid choice...")
        
        
        
        
        
# emp = {}

# ch = 0
# while(ch != '6'):
#     print('''Please select option from below:
#     1. Add employee
#     2. Update employee
#     3. Delete employee
#     4. Search employee
#     5. Show all employees
#     6. Exit
#     ''')
#     ch = input("Enter choice:")
    
#     if(ch == '1'):
#         id = input("Enter eid:")
#         if id in emp.keys():
#             print("Employee ID already exists!")
#         else:
#             name = input("Enter ename:")
#             sal = float(input("Enter salary:"))
#             eData = f'{id}, {name}, {sal}'
#             emp[id] = eData
#             print("Employee added successfully....")
        
#     elif(ch == '2'):
#         id = input("Enter id for updating employee detail:")
#         if(id in emp.keys()):
#             eData = emp[id]
#             eList = eData.split(', ')
#             chk = input("Do you want to change name(y/n):")
#             if(chk.lower() in ['y', 'yes']):
#                 eList[1] = input("Enter new name:")
#             chk = input("Do you want to change salary(y/n):")
#             if(chk.lower() in ['y', 'yes']):
#                 eList[2] = input("Enter new salary:")
#             eData = ', '.join(eList)
#             emp[id] = eData
#             print("Data updated successfully....")
#         else:
#             print("Employee id not found.")
    
#     elif(ch == '3'):
#         id = input("Enter id to delete:")
#         if(id in emp.keys()):
#             removed = emp.pop(id)   
#             print(f"Employee deleted successfully. {removed}")
#         else:
#             print("Employee id not found.")
    
#     elif(ch == '4'):
#         id = input("Enter id to search:")
#         if(id in emp.keys()):
#             print(f"Employee found: {emp[id]}")
#         else:
#             print("Employee id not found.")
    
#     elif(ch == '5'):
#         if emp:
#             print("\n--- All Employees ---")
#             for k, v in emp.items():
#                 print(f"{k} -> {v}")
#         else:
#             print("No employees found.")
    
#     elif(ch == '6'):
#         print("Thank you for choosing us!")
#     else:
#         print("Invalid choice...")
