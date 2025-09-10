# Create a class Product with members as pid,pname,price and quantity .Add ollowing methods:
# d. Constructor (Support both parameterized and parameterless)
# e. Destructor
# f. ShowBook


class Product:
    def __init__(self,pid=0,pname="na",price=0,quantity=0):
        self.id=pid
        self.name=pname
        self.price=price
        self.qty=quantity
        print("Constructor called..")

    def showBook(self):
        print("Product id:",self.id)
        print("Product name:",self.name)
        print("Product price:",self.price)
        print("Product quantity:",self.qty)
    
    def __del__(self):
        print("Destructor called...")

p1=Product(101,"Pirates Of The Caribbean",3000,2)
p1.showBook()

p2=Product()
p2.showBook()
