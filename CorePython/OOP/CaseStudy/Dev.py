from Emp import Emp

class Dev(Emp):
    def __init__(self, id, nm, basic,bonus):
        super().__init__(id, nm, basic,"S/W Developer")
        self.bonus=bonus
    
    def calSal(self):
        da=self.basic*0.1
        hra=self.basic*0.12

        self.total_sal=self.basic+da+hra+self.bonus
        # print(self.total_sal)

    


# d1=Dev(101,"ABC",10000,5000)
# d1.calSal()
# print(d1)