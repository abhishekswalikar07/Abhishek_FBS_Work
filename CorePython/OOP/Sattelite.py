class Satellite:
    def setData(self,name,weight,camera):
        self.n=name
        self.w=weight
        self.c=camera
    def display(self):
        print("Name:",self.n)
        print("Weight:",self.w)
        print("Camera:",self.c)
    def launch(self):
        print("After launching satellite into sapce, satellites collets the information of the globe and send to receivers..")
        
    def use(self):
        print("Satellites are used to gather latest data about new thing or research on new objects")
        
s=Satellite()
s.setData("PSLV",1200,"0.7 GSD")
s.display()
s.launch()
s.use()