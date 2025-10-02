from Emp import Emp

class Admin(Emp):
    def __init__(self, id, nm, basic,allowance):
        super().__init__(id, nm, basic,"Admin")
        self.allowance=allowance
    
    def calSal(self):
        da=self.basic*0.1
        hra=self.basic*0.12

        self.total_sal=self.basic+da+hra+self.allowance
        # print(self.total_sal)

# a1=Admin(101,"ABC",10000,5000)
# a1.calSal()
# print(a1)