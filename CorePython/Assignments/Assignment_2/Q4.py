# WAP to calculate area of triangle and rectangle

a=float(input("Enter the height for triangle and lenght for rectangle:"))
b=float(input("Enter the base for triangle and breadth for rectangle:"))

triangle_area=0.5*a*b
rectangle_area=a*b

print(f'Area of triangle of base {b} and height {a} is {triangle_area}.')
print(f'Area of triangle of breadth {b} and length {a} is {rectangle_area}.')