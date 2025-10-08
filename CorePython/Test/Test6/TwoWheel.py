from Vehicle import Vehicle

class TwoWheel(Vehicle):
    def __init__(self, num, persons):
        super().__init__(num, "Two Wheeler", basic=20)
        self.persons = persons

    def caltoll(self):
        if self.persons > 2:
            self.totalToll = self.basic + (self.persons * 10)
        else:
            self.totalToll = self.basic
