l=int(input("Enter length of the wall:"))
b=int(input("Enter breadth of wall:"))

Area_Wall=l*b*15

cost_per_sq_ft=float(input("Enter cost per square feet:"))

Total_cost=Area_Wall*cost_per_sq_ft

print(f'Total cost to paint the whole building wall is {Total_cost} Rs.')
