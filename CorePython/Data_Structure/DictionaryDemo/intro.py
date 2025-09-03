#1. structure : {}
# d = {1:'Python', 2:'Java', 3:'C'}
# print(type(d))

#2. Types of data : pair of key : value - heterogenous
# d = {1:'Python', 'course':[1,2,3]}
# print(type(d))

#3. Sequence : Ordered
# print(d)

#4. Changable : Key is immutable, Value is Mutable
# d[1] = 'Core python'
# print(d)

#5. Only immutable ds can be allowed as key
# d1 = {'name':'ABC', [1, 2]:'XYZ'}

#6. Keys should be unique, duplicate values are be allowed
d2 = {1:'Python', 2:'Java', 2:'C'}
print(d2)