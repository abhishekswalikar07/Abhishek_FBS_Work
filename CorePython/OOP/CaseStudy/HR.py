from Emp import Emp

class HR(Emp):
    def __init__(self, id, nm, basic,comm):
        super().__init__(id, nm, basic,"HR")
        self.comm=comm
    
    def calSal(self):
        da=self.basic*0.1
        hra=self.basic*0.12

        self.total_sal=self.basic+da+hra+self.comm
        # print(self.total_sal)

# h1=HR(101,"ABC",10000,5000)
# h1.calSal()
# print(h1)

