class Trees:
    def setData(self,name,size,fruit):
        self.n=name
        self.s=size
        self.f=fruit
    def display(self):
        print("Name:",self.n)
        print("Size:",self.s)
        print("Fruit:",self.f)
        
    def breath(self):
        print("Trees generates oxygen for living organisms to breath and provide fruits for eat.")
    def use(self):
        print("Trees are very useful as they maintain the balance of nature and creates living environment for living things")
    
t=Trees()
t.setData("Mango","Big","Mango")
t.display()
t.breath()
t.use()