li1=[1,2,3,4]
li2=[3,2,5,8]

li3=[]
print(f'Unoin of {li1} and {li2} is :')
for i in li1:
    li3.append(i)
    
for j in li2:
    li3.append(j)
    
# print(li3)

li3=set(li3)

print(list(li3))