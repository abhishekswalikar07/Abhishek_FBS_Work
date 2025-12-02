class Emp:
    def __init__(self,eid,ename,basic):
        self.id=eid
        self.name=ename
        self.basic=basic
    
    def __str__(self):
        return f'{self.id}, {self.name}, {self.basic}'