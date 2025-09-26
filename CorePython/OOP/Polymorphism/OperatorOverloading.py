class Time:
    def __init__(self,h,m,s):
        self.h=h
        self.m=m
        self.s=s
    def __add__(self,other):                     
        s=self.s+other.s
        m=s//60
        s=s%60
        
        m=self.m+other.m+m
        h=m//60
        m=m%60
        h=self.h+other.h+h
        return f"{h} hours: {m} minutes: {s} seconds"
    

t1=Time(35,43,29)
t2=Time(20,34,55)
print(t1+t2)


