class Shirt:
    # constructor (parameterless + parameterized)
    def __init__(self, sid=0, sname="Unknown", stype="Casual", price=0.0, size="Small"):
        self.sid = sid
        self.sname = sname
        self.stype = stype
        self.price = price
        self.size = size.capitalize()  
        print("Constructor Called. Shirt Created.")

    # destructor
    def __del__(self):
        print("Destructor Called. Shirt Destroyed.")

    def get_price_by_size(self):
        if self.size == "Small":
            return self.price
        elif self.size == "Medium":
            return self.price * 1.10  
        elif self.size == "Large":
            return self.price * 1.20  
        else:
            return self.price  

   
    @staticmethod
    def show_shirt(Shirt):
        print(f"\nShirt ID: {Shirt.sid}")
        print(f"Shirt Name: {Shirt.sname}")
        print(f"Type: {Shirt.stype}")
        print(f"Base Price: {Shirt.price}")
        print(f"Size: {Shirt.size}")
        print(f"Price (with size adjustment): {Shirt.get_price_by_size()}")

   
s1 = Shirt()
Shirt.show_shirt(s1)   # static method call

# parameterized constructor (small)
s2 = Shirt(101, "Arrow Classic", "Formal", 1000, "Small")
Shirt.show_shirt(s2)

# medium (10% extra)
s3 = Shirt(102, "Levis Denim", "Casual", 1000, "Medium")
Shirt.show_shirt(s3)

# large (20% extra)
s4 = Shirt(103, "Peter England", "Formal", 1000, "Large")
Shirt.show_shirt(s4)

del s4
