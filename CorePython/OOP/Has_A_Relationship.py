from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self,name,age,type):
        self.name=name
        self.age=age
        self.type=type

    @abstractmethod
    def sound():
        pass

class Dog(Animal):
    def __init__(self, name, age, type,breed):
        super().__init__(name, age, type)
        self.breed=breed
    
    def sound(self):
        print("Dog  is barking..")
    
class Tiger(Animal):
    def __init__(self, name, age, type,strips):
        super().__init__(name, age, type)        
        self.strips=strips
    
    def sound(self):
        print("Tiger is roaring...")
    

d1=Dog("Dogesh Bhai",2,"Pet","Husky")

t1=Tiger("Sherkhan",20,"Wild","Brown Black")

li_obj=[d1,t1]
for obj in li_obj:
    obj.sound()                                            
