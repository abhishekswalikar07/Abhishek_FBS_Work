from Dev import Dev
from HR import HR
from Admin import Admin

class Emp:
    emp_details={}

    def addEmp():
        id = input("Enter id: ")
        if id in Emp.emp_details:
            print("Employee with this ID already exists!")
            return

        name = input("Enter name: ")
        basic = float(input("Enter basic salary: "))

        print("""Please select option from below:
            1. S/W Developer
            2. HR
            3. Admin""") 
        ch = input("Enter choice: ")

        if ch == "1":
            bonus = float(input("Enter bonus: "))
            emp = Dev(id, name, basic, bonus)
        elif ch == "2":
            comm = float(input("Enter Commission: "))
            emp = HR(id, name, basic, comm)
        elif ch == "3":
            allowance = float(input("Enter allowance: "))
            emp = Admin(id, name, basic, allowance)
        else:
            print("Invalid choice.")
            return

        emp.calSal()
        Emp.emp_details[id] = emp
        print("Employee added successfully.")


    # def addEmp():
    #     # print("This is employee add method...")

    #     id = input("Enter id: ")
    #     if id in Emp.emp_details:
    #         print("Employee with this ID already exists!")
    #         return

    #     name=input("Enter name:")
    #     basic=float(input("Enter basic salary:"))

    #     ch=0
    #     print("""Please select option from below:
    #           1. S/W Developer
    #           2. HR
    #           3. Admin""") 
    #     ch=input("Enter choice:")

    #     if ch=="1":
    #         bonus=float(input("Enter bonus:"))
    #         d1=Dev(id,name,basic,bonus)
    #         d1.calSal()
    #         edata=str(d1)
    #     elif ch=="2":
    #         comm=float(input("Enter Commision:"))
    #         h1=HR(id,name,basic,comm)
    #         h1.calSal()
    #         edata=str(h1)
    #     elif ch=="3":
    #         allowance=float(input("Enter allowance:"))
    #         a1=Admin(id,name,basic,allowance)
    #         a1.calSal()
    #         edata=str(a1)
        
    #     Emp.emp_details[id]=edata 
    #     print("Employee added successfully...")
        
    def updEmp():
        id=input("Enter employee id to update:")
        if id  in Emp.emp_details:
            emp=Emp.emp_details[id]
            print(f"Employee current details: {emp}")
            nm=input("Enter new name for employee(for same leave blank):")
            if nm.strip():
                emp.name=nm
            new_basic = input("Enter new basic salary (leave blank to keep same): ")
            if new_basic.strip():
                if new_basic.replace('.', '', 1).isdigit():  # check number (allow decimal)
                    emp.basic = float(new_basic)
                else:
                    print("Invalid salary input. Keeping old salary.")

            emp.calSal()  # recalculate
            print("Employee updated successfully.")
        else:
            print("Employee not found.")

    def delEmp():
        id = input("Enter employee id to delete: ")
        if id in Emp.emp_details:
            del Emp.emp_details[id]
            print("Employee deleted successfully.")
        else:
            print("Employee not found.")

    def showAllEmp():
        if not Emp.emp_details:
            print("No employees found.")
            return

        print("\n===== Employee List =====")
        print("{:<10}{:<15}{:<12}{:<15}".format("ID", "Name", "Salary", "Designation"))
        print("-" * 55)
        for emp in Emp.emp_details.values():
            print("{:<10}{:<15}{:<12}{:<15}".format(emp.id, emp.name, emp.total_sal, emp.dept))

    def searchEmp():
        id = input("Enter employee id to search: ")
        if id in Emp.emp_details:
            print("Employee Found:", Emp.emp_details[id])
        else:
            print("Employee not found.")

    