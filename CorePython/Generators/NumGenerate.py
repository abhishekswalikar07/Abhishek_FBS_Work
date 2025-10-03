def number(num):
    for i in range(1,num+1):
        yield i
res=number(100)
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
