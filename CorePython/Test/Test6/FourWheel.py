from Vehicle import Vehicle

class FourWheel(Vehicle):
    def __init__(self, num, persons):
        super().__init__(num, "Four Wheeler", basic=40)
        self.persons = persons

    def caltoll(self):
        if self.persons > 4:
            self.totalToll = self.basic + (self.persons * 40)
        else:
            self.totalToll = self.basic
