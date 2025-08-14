# Write a program to calculate the total cost of painting. The interior of building with four
# equal sized walls.


l=int(input("Entder length of wall in meter:"))
b=int(input("Entder breadth of wall in meter:"))

area=l*b

total_area=area*4   

cost=float(input("Enter cost of painting per sq. meter :"))

total_cost=total_area*cost

print(f'Total cost for 4 walls of area {total_area} sq. m is {total_cost} Rs')

