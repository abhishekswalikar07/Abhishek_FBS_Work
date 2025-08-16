# Program to print hollow triangle pattern

for i in range(1,6):
    for j in range(i,6):
        if (i==2 and (j==3 or j==4) or i==3 and j==4):
            print(' ',end=' ')
        else:
            print(j,end=' ')
    print()


