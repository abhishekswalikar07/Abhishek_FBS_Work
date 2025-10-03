def myDecorator(fun):
    def wrapper():
        print("This is wrapper function...")
        fun()
        print("This is end..")
    return wrapper
@myDecorator
def greet():
    print("Good morning...")

greet()



# fun=greet
#greet=wrapper

#great()
