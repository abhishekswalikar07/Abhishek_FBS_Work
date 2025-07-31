l=int(input("Enter length of rectangle:"))
b=int(input("Enter breadth of rectangle:"))
r=int(input("Enter radius of circle:"))

Area_rectangle=l*b
perimeter_rectangle=2*(l+b)

Area_Circle=(3.14*r*r)/2
Perimeter_circle=3.14*r

Total_Area=Area_rectangle+Area_Circle
Total_Perimeter=perimeter_rectangle+Perimeter_circle

print(f'Total Area of the given figure is {Total_Area}.')

print(f'Total perimeter of given figure is {Total_Perimeter}')
