# 7. Python Program to Find the Intersection of Two Lists
def intersect_of_list(li1,li2):
    intersect = []
    for ele in li1:
        if ele in li2:
            intersect.append(ele)
    return intersect

li1 = [9,2,3,4,5,6]
li2 = [4,5,6,7,8,9]
res = intersect_of_list(li1,li2)
print(f'the Intersection of Two Lists: {res}')