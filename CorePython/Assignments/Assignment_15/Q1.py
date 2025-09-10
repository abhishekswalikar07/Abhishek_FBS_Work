# Create a class Book with members as bid,bname,price and author.Add following methods:
# a. Constructor (Support both parameterized and parameterless)
# b. Destructor
# c. ShowBook


class Book:
    def __init__(self, bid=0,bname="na",price=0,author=""):
        self.id=bid
        self.name=bname
        self.price=price
        self.author=author
        print("Instructor called")
    def showBook(self):
        print("Book id:",self.id)
        print("Book name:",self.name)
        print("Book price:",self.price)
        print("Book author:",self.author)

    def __del__(self):
        print("Destructor is called")

b1=Book(101,"Harry Potter",4000,"J. K. Rowling")
b1.showBook()

b2=Book()
b2.showBook()


        