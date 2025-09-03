# 6. Python Program to Find the Union of two Lists
def union_of_list(li1,li2):
    union = []
    for ele in li1+li2:
        if ele not in union:
            union.append(ele)
    return union

li1 = [1,2,3,4,5,6]
li2 = [4,5,6,7,8,9]
res = union_of_list(li1,li2)
print(f'the Union of two Lists: {res}')