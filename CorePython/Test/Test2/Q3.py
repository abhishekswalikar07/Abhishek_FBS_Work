# A farmer has a field which is half in circle share and rest rectangle. He needs to do fencing
# for entire field using barbed wire 5 times. Circular section has radius 20m and rectangle
# length is 50 m and breadth is 40m. If cost of barbed wire is 35Rs/m then calculate the total
# cost of fencing the field.

r=20
l=50 
b=40

peri_circle=(3.14*r)
peri_rectangle=2(l+b)

total_peri=peri_circle+peri_rectangle

cost=total_peri*35

total_cost=cost*5

print(f'Total cost for fencing the field of {total_peri} sq.m is {total_cost} Rs')
