def selectionSort(li):
    for i in range(0,len(li)-1):
        ind=i
        for j in range(i+1, len(li)):
            if li[j]<li[ind]:
                ind=j
            li[i],li[ind]=li[ind],li[i]
    return li
li=[60,50,40,30,20,10]
print("List before sort:",li)
li=selectionSort(li)
print("List after sort:",li)