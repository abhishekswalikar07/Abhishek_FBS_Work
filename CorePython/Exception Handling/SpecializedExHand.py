try:
    li=[10,20,30,40]
    print(li)
    ind=int(input("Enter index to pop the element:"))
    li.pop(ind)
    print(li)
    ele=int(input("Enter value to check index:"))
    print("Index:",li.index(ele))
    del li
    print(li)
except IndexError : # Specialized exception handling
    print("index error is occured.")
except ValueError: # Specialized exception handling
    print("value error is occured.. ")
except NameError:  # Specialized exception handling
    print("Name error occured..")
except: # Generalized exception handling
    print("Something went wrong..")

