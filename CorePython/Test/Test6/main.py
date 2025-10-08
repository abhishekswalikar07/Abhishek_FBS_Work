from VehicleManage import VehicleManage
from TwoWheel import TwoWheel
from ThreeWheel import ThreeWheel
from FourWheel import FourWheel
from HeavyVehicle import HeavyVehicle

def login():
    admin = "admin"
    password = "1234"

    adminid = input("Enter admin id: ")
    passwd = input("Enter password: ")

    if adminid != admin or passwd != password:
        print("Invalid credentials...")
        return
    print("Login successful...")

    ch = "0"
    while ch != "6":
        print("""
Please select option from below:
    1. Two Wheeler
    2. Three Wheeler
    3. Four Wheeler 
    4. Heavy Vehicle 
    5. Show Vehicle
    6. Exit 
""")
        ch = input("Enter choice: ")

        if ch == "1":
            VehicleManage.add_vehicle(TwoWheel)
        elif ch == "2":
            VehicleManage.add_vehicle(ThreeWheel)
        elif ch == "3":
            VehicleManage.add_vehicle(FourWheel)
        elif ch == "4":
            VehicleManage.add_vehicle(HeavyVehicle)
        elif ch == "5":
            VehicleManage.show_vehicle()
        elif ch == "6":
            print("Thank you...")
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    ch = "0"
    while ch != "2":
        print(''' 
Please select option from below:
    1. Login
    2. Exit
''')
        ch = input("Enter choice: ")

        if ch == "1":
            login()
        elif ch == "2":
            print("Thank you...")
        else:
            print("Invalid choice...")
