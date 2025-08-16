#  Write a program to calculate area of circle

def areaCircle(r):
    area=0
    area=3.14*r*r
    print(f'Area of circle of radius {r} is {area}')
    
a=int(input("Enter radius of circle:"))

areaCircle(a)