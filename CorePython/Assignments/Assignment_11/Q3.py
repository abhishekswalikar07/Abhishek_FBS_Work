# 3. Python Program to Sort the List According to the Second Element in Sublist
li = [[1, 4], [3, 2], [5, 6], [7, 1,5]]

for i in range(len(li)):
    for j in range(0, len(li) - i-1):
        if li[j][1] > li[j + 1][1]:
            li[j], li[j + 1] = li[j + 1], li[j]

print(li)