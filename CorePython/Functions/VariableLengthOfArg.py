#1. Mentioned asterik(*) symbol before paraameter in function definition.
#2. Can pass multiple values in function call
#3. Store in tuple format


def add(*data):
    sum=0
    for ele in data:
        sum+=ele
    print(sum)
    
add(10,20)
add(1,2,3,4,5,6,7,8,9,10)