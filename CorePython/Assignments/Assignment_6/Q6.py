
for i in range(1,6):
    for j in range(1,6-i):
        print("  ", end=" ")
    k=1 
    for j in range(1,2*i):
        print(k, end="  ")
        k+=1   
    print()