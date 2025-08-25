li=[10,30,50,20,40]

max=li[0]

for i in range(1,len(li)):
    if li[i]>max:
        max=li[i]
print("Maximum number is:",max)