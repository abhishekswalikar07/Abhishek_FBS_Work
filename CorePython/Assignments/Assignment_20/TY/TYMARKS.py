from SY.SYMARKS import SYMARKS

class TYMARKS(SYMARKS):
    def __init__(self, CSTotal=0, MathTotal=0, ElecTotal=0,Theory=0,Practical=0):
        super().__init__(CSTotal, MathTotal, ElecTotal)
        self.theory=Theory
        self.practical=Practical
    
    def TotalMarks(self):
        self.Total=self.cs+self.math+self.elec+self.theory+self.practical
    
    