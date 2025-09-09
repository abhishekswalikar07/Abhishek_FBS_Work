d=[1,3,4,1,2,3,6,7,1,2,4]
count=0
occur={}

for i in d:
    count=d.count(i)
    occur.update({i:count})
print(occur)