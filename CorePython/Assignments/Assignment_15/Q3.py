# Create a class Shirt with members as sid,sname,type(formal etc), price and
# size(small,large etc) .Add following methods:
# g. Constructor (Support both parameterized and parameterless)
# h. Destructor
# i. ShowBook


class Shirt:
    def __init__(self, sid=0,sname="na",type="Formal",size=""):
        self.id=sid
        self.name=sname
        self.type=type
        self.size=size
        print("Constructor called")

    def showShirt(self):
        print("Shirt id:",self.id)
        print("Shirt name:",self.name)
        print("Shirt type:",self.type)
        print("Shirt size:",self.size)

    def __del__(self):
        print("Destructor called")


s1=Shirt(1,"US POLO","Casual","XL")
s1.showShirt()

s2=Shirt()
s2.showShirt()
    
