def add(x,y):
    print(x+y)
# print(id(add))
demo=add
del add
demo(10,20)
# print(id(demo))