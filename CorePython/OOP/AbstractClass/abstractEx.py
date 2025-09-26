from abc import ABC, abstractmethod

class Vehicle(ABC):
# Can't create object of abstract class
    @abstractmethod
    def stop():
        pass

class Bike(Vehicle):

    def start(self):
        print("Bike started..")

    def stop(self):
        print("Bike stopped..")

b1=Bike()
b1.start()
b1.stop()
