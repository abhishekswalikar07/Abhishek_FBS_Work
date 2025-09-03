# 5. Python Program to Sort a List According to the Length of the Elements
# within the list.
li = [[1,2,3],[1,34],[1,2,3,4],[2],[]]

for i in range(len(li)):
    for j in range(len(li)-i-1):
        if len(li[j])>len(li[j+1]):
            li[j],li[j+1]=li[j+1],li[j]
print(li)