class Fan:
    def setData(self,brand,color,price):
        self.b=brand
        self.c=color
        self.p=price
        
        
    def display(self):
        # print("Display Method")
        print("Brand:",self.b)
        print("Color:",self.c)
        print("Price:",self.p)
        
    def start(self):
        print("Fan gets started on turning on ")
        
    def regulate(self):
        print("On switching regulator from left to right the speed of fan increases and on swi switching regulator from right to left the speed of fan decreases")
        
    def turnOff(self):
        print("Fan gets stopped on switching off ")
        
obj1=Fan() 
obj1.setData("Godrej","White",2500)
obj1.display()
obj1.start()
obj1.regulate()
obj1.turnOff


# obj1.setData("Bajaj","Black",4000)
# obj1.display()

