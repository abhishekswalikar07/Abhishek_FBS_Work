li=[10,30,50,20,40]

min=li[0]

for i in range(1,len(li)):
    if li[i]<min:
        min=li[i]
print("Minimum number is:",min)