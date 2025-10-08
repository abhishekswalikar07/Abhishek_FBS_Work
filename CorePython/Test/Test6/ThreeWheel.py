from Vehicle import Vehicle

class ThreeWheel(Vehicle):
    def __init__(self, num, persons):
        super().__init__(num, "Three Wheeler", basic=30)
        self.persons = persons

    def caltoll(self):
        if self.persons > 3:
            self.totalToll = self.basic + (self.persons * 20)
        else:
            self.totalToll = self.basic
