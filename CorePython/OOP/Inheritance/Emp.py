class Employee:
    def __init__(self,id,nm,sal):
        self.eid=id
        self.ename=nm
        self.salary=sal
    
    def displayData(self):
        print("Id:",self.eid)
        print("Name:",self.ename)
        print("Salary:",self.salary)
    
    def showData(self):
        print("This is show data method")

class SalesMang(Employee):
    def __init__(self, id, nm, sal,tar,inc):
        super().__init__(id, nm, sal)
        self.target=tar
        self.incentives=inc
    
    def displayData(self):
        super().displayData()
        print("Target:",self.target)
        print("Incentives:",self.incentives)

    def __del__(self):
        print("Destructor called...")


sm1=SalesMang(101,"Sachin",50000,10,10000)
sm1.displayData()
sm1.showData()