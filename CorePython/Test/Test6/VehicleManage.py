from TwoWheel import TwoWheel
from ThreeWheel import ThreeWheel
from FourWheel import FourWheel
from HeavyVehicle import HeavyVehicle

class VehicleManage:
    vehicle_details = {}

    @staticmethod
    def add_vehicle(vehicle_class):
        num = input("Enter vehicle number: ")
        if num in VehicleManage.vehicle_details:
            print("Vehicle with this number already exists.")
            return

        persons = int(input("Enter number of persons: "))

        # vehicle_class automatically knows its type and basic toll
        vehiType = vehicle_class(num, persons)
        vehiType.caltoll()

        VehicleManage.vehicle_details[num] = vehiType
        print(f"Toll generated successfully!")
        # print(f"Vehicle Type: {vehiType.vtype}")
        # print(f"Basic Toll: {vehiType.basic}")
        # print(f"Total Toll: {vehiType.totalToll}")

    @staticmethod
    def show_vehicle():
        if not VehicleManage.vehicle_details:
            print("No vehicles found.")
            return

        print("\n===== Vehicle List =====")
        print("{:<12}{:<15}{:<12}{:<10}".format("Number", "Type", "Total Toll", "Persons"))
        print("-" * 55)
        for vehi in VehicleManage.vehicle_details.values():
            print("{:<12}{:<15}{:<12}{:<10}".format(
                vehi.num, vehi.vtype, vehi.totalToll, vehi.persons
            ))
