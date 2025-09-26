class Emp:
    def __init__(self,id,name,sal,dept):
        self.eid=id
        self.ename=name
        self.sal=sal
        self.dept=dept
    
    def __str__(self):
        return f"{self.eid}, {self.ename}, {self.sal}, {self.dept}"
    
e1=Emp(101,"Abhishek",50000,"Business Analyst")
print(e1)