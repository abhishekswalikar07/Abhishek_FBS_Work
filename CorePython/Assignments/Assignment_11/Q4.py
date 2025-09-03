# 4. Python Program to Find the Second Largest Number in a List Using Bubble Sort
def sec_larg_num_sort(li):
    for i in range(1,3):
        for j in range(len(li)-i):
            if li[j]>li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]

    return li[-2]
li = [50,2,9,7,1,60,3,100,24,88]
res = sec_larg_num_sort(li)
print(f'the Second Largest Number in a List is: {res}')