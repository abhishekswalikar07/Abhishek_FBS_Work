
#Write a program to enter P, T, R and calculate Compound Interest 

p=int(input("Enter principle value:"))
r=int(input("Enter rate value:"))
t=int(input("Enter time (in year) value:"))

CI = p* ((1 + (r / 100)) ** t)- p
print(f'Compound interest for principle {p}, rate {r} and time {t} is {CI}')