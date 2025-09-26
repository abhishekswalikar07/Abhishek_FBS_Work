class Person:
    def __init__(self,nm,age,add):
        self.name=nm
        self.age=age
        self.address=add

    def displayData(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Address",self.address)

# p1=Person("Abhi",23,"Sangli")
# p1.displayData()