def linearSearch(li, searchEle):
    for ind in range(len(li)):
        if li[ind]==searchEle:
            return ind
    else:
        return -1
li=[12,35,8,84,53]
searchEle=int(input("Enter number to search:"))
res=linearSearch(li,searchEle)
if res != -1:
    print(f'{searchEle} is found at index {res}')
else:
    print(f'{searchEle} is not found in the list')