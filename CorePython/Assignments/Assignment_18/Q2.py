# Create a class Distance with data members as km,m and cm and add following
# methods :
# a. Constructor
# b. Destructor
# c. Overload +,- operator


class Distance:
    def __init__(self,km,m,cm):
        self.km=km
        self.m=m
        self.cm=cm
        print("Constructor called...")
    
    def __add__(self,other):
        cm=self.cm+other.cm
        m=cm//100
        cm=cm%100

        m=self.m+other.m+m
        km=m//1000
        m=m%1000

        km=self.km+other.km+km

        return f'{km} km : {m} m : {cm} cm'
    def __del__(self):
        print("Destructor called!!!")



d1=Distance(10,400,85)
d2=Distance(12,800,60)
print(d1+d2)
