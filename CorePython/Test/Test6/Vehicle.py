from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, num, vtype, basic):
        self.num = num
        self.vtype = vtype
        self.basic = basic
        self.totalToll = 0

    @abstractmethod
    def caltoll(self):
        pass

    def __str__(self):
        return f'{self.num}, {self.vtype}, {self.totalToll}'
