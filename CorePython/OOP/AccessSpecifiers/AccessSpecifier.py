class Emp:
    def __init__(self,id,name,sal):
        self.id=id       # public
        self._name=name  # protected
        self.__sal=sal   # private

e1=Emp(101,"Abhi",70000)
print(e1.id)
# print(e1.name)
print(e1._name)
# print(e1.__sal)  
print(e1._Emp__sal)

