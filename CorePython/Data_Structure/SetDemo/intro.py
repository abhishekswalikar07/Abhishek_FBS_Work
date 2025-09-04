#1. Structure: {} with only values ... For blank set use set()

s={1,'a',3.14,2,'b'}

print(type(s)) 

# s=set()
# print(type(s))

# 2. Type of data: Heterogeneous


# 3. Sequence: Unordered

# print(s)

# 4. Changable: Mutable but not editable

s.add(50)
# print(s)


# 5. Unique elements are present
s.add(2)
print(s)
