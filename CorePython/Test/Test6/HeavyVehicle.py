from Vehicle import Vehicle

class HeavyVehicle(Vehicle):
    def __init__(self, num, persons):
        super().__init__(num, "Heavy Vehicle", basic=60)
        self.persons = persons

    def caltoll(self):
        if self.persons > 6:
            self.totalToll = self.basic + (self.persons * 100)
        else:
            self.totalToll = self.basic
