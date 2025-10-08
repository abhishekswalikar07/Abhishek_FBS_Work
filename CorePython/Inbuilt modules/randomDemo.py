import random

print(random.random())
print(random.randint(1,1000))
li=[1,2,3,4,5,6]
# li=range(1,7)
print(random.choice(li))
random.shuffle(li)
print(li)
print(random.uniform(1.0,5.0))
print(random.sample(li,2))