# 1. Python Program to Put Even and Odd elements of a List into two Different
# Lists

def seperate_even_odd(li):
    li1 = list(map(lambda x: x%2==0 , li))
    even = []
    odd = []
    for i in range(len(li)):
        if li1[i]:
            even.append(li[i])
        else:
            odd.append(li[i])
    print("Even numbered list:",even)
    print("Odd numbered list:",odd)


li = [1, 2, 34, 45, 42, 432, 324, 6, 78, 42, 9, 352, 7, 89, 42]
seperate_even_odd(li)
