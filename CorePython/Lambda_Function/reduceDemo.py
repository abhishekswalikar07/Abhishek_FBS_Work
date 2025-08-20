

import functools
num=[34,57,84,33,92,28,65,77]

res=functools.reduce(lambda x,y:x+y, num)
print(res)