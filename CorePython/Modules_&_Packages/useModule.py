#1. Method 1
import function
print(function.add(25,18))

#2. method 2
from function import *
print(add(10,20))

#3. Method 3
from function import add,fact
print(add(20,30))


#4. method 4- Alias name
from function import chkEven as ck
print(ck(5))
