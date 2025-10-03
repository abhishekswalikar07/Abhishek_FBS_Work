def prime():
    num=2
    while True:
        for i in range(2, (num//2)+1):
            if num%i==0:
                break
        else:
            yield num
        num+=1
res=prime()
for i in range(10):
    print(next(res))


print("##### Second Method #####")
def prime_generator():
    num = 2
    while True:   
        for i in range(2, int(num//2) + 1):
            if num % i == 0:
                break
        else:
            yield num  
        num += 1

res = prime_generator()
print(next(res))  
print(next(res)) 
print(next(res)) 
print(next(res))

            