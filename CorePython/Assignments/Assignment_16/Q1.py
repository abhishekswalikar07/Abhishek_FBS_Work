class Book:
    count = 0
    def __init__(self, bid=0, bname="", price=0, author=""):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author
        Book.count += 1
        print("Constructor Called. Object Created.")

    def __del__(self):
        print("Destructor Called. Object Destroyed.")

    def show_book(self):
        print(f"Book ID: {self.bid} \nBook Name: {self.bname} \nPrice: {self.price} \nAuthor: {self.author}")


    @staticmethod
    def show_count():
        print(f"Total Books Created: {Book.count}")


b1 = Book()
b1.show_book()
Book.show_count()
print("##########")
b2 = Book(101, "Python Crash Course", 450.75, "Eric Matthes")
b2.show_book()
Book.show_count()
print("##########")
b3 = Book(102, "Fluent Python", 699.99, "Luciano Ramalho")
b3.show_book()
Book.show_count()

del b3
Book.show_count()
