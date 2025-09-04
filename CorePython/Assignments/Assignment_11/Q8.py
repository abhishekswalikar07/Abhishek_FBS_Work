# 8. Print 1 to 100 in snakes and ladder pattern.
num = 1
for i in range(100,0,-10):
    if num%2!=0:
        for j in range(i,i-10,-1): 
            print(j,end=' ')
    else:
        for k in range(i-9,i+1,+1):
            print(k, end=' ')

    num+=1
    print()
    
    
# board=[]
# for i in range(9,-1,-1):
#     row=[]
    
#     for j in range((i*10)+1, (i*10)+11):
        # print(j,end=" ")
#         row.append(j)
    # print()
#     if i%2!=0:
#         row.reverse()
#     board.append(row)
# print(board)