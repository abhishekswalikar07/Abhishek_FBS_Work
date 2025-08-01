# Write a program to enter P, T, R and calculate simple Interest.

p=int(input("Enter principle value:"))
r=int(input("Enter rate value:"))
t=int(input("Enter time (in year) value:"))

SI=(p*r*t)/100
print(f'Simple interest for principle {p}, rate {r} and time {t} is {SI}')

    