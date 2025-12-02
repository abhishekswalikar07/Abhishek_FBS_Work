from Emp import Emp
class EmpManage:
    emp_details={}
    def addEmp():
        id=input("Enter employee id:")
        if id in EmpManage.emp_details:
            print("Employee with this ID already existed")
            return
        name=input("Enter Employee name:")
        basic=float(input("Enter employee basic price:"))
        emp = Emp(id, name, basic)
        with open("CorePython/Assignments/Assignment_22/Emp.txt", "a") as f:
            f.write(str(emp) + "\n")
        print("Record added successfully.")

    def searchEmp():
        id=input("Enter id of employee for search:")
        Found=False
        try:
            with open('CorePython/Assignments/Assignment_22/Emp.txt','r') as fp:
                for line in fp:
                    empid,ename,ebasic=line.strip().split(", ")
                    if empid==id:
                        print(f"Record Found → ID: {empid}, Name: {ename}, Salary: {ebasic}")
                        Found=True
                        break
            if not Found:
                print("Employee record not found...")
        except FileNotFoundError :
            print("File not found")
        # except Exception as e:
        #     print("Error:",e)

    def delEmp():
        id=input("Enter id of employee for delete:")
        found=False
        try:
            with open('CorePython/Assignments/Assignment_22/Emp.txt','r') as fp:
                lines=fp.readlines()

            with open('CorePython/Assignments/Assignment_22/Emp.txt','w') as fp:
                for line in lines:
                    empid,ename,ebasic=line.strip().split(", ")
                    if empid!=id:
                        fp.write(line)
                    else:
                        found=True
            if found:
                print("Employee record deleted  successfully..")
            else:
                print("Employee record not found...")
        except FileNotFoundError:
            print("File not found...")
        

    def updEmp():
        eid = input("Enter Employee ID to update: ")
        found = False
        try:
            with open("CorePython/Assignments/Assignment_22/Emp.txt", "r") as fp:
                lines = fp.readlines()

            with open("CorePython/Assignments/Assignment_22/Emp.txt", "w") as fp:
                for line in lines:
                    empid, ename, ebasic = line.strip().split(", ")
                    if empid == eid:
                        print("Enter new details:")
                        name = input("Enter new name: ")
                        basic = input("Enter new basic salary: ")
                        emp = Emp(eid, name, basic)
                        fp.write(str(emp) + "\n")
                        found = True
                    else:
                        fp.write(line)
            if found:
                print("✅ Record updated successfully.\n")
            else:
                print("❌ Employee not found.\n")
        except FileNotFoundError:
            print("❌ File not found.\n")

    def DisplayEmp():
        try:
            with open("CorePython/Assignments/Assignment_22/Emp.txt", "r") as fp:
                data = fp.readlines()
                if not data:
                    print("⚠️ No records found.\n")
                    return
                print("\n--- Employee Records ---")
                for line in data:
                    empid, ename, ebasic = line.strip().split(", ")
                    print(f"ID: {empid}   | Name: {ename}    | Basic: {ebasic}")
                print("------------------------------\n")
        except FileNotFoundError:
            print("❌ File not found.\n")

# e=EmpManage()
# e.delEmp()