def myDecorator(fun):
    def wrapper(x,y):
        print("Addition is:")
        fun(x,y)
    return wrapper

@myDecorator
def add(x,y):
    print(x+y)

add(10,20)