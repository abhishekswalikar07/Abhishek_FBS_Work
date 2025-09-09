data=[[101,"Seema",45000],
      [340,"Rajani",13000],
      [210,"Tannu",14000],
      [320,"Suresh",35000]]


for i in range(1,len(data)):
    for j in range(0, len(data)-i):
        if data[j][2]>data[j+1][2]:
            data[j][2],data[j+1][2]=data[j+1][2],data[j][2]
print(data)
        


