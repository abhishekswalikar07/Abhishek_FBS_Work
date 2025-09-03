# 8. Print 1 to 100 in snakes and ladder pattern.
num = 1
for j in range(100,0,-10):
    if num%2!=0:
        for i in range(j,j-10,-1): 
            print(i,end=' ')
    else:
        for k in range(j-9,j+1,+1):
            print(k, end=' ')

    num+=1
    print()