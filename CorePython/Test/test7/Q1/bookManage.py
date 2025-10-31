from Book import Book

class BookManage:
    book_details={}

    def addBook():
        id=input("Enter book id:")
        if id in BookManage.book_details:
            print("Book with this ID already existed")
            return
        name=input("Enter book name:")
        price=float(input("Enter book price:"))
        author=input("Enter book author:")

        b1=Book(id,name,price,author)
        print(b1)
        BookManage.book_details[id]=b1
        print("Book added successfully")

    def delBook():
        id =input("Enter book id to delete:")
        if id in BookManage.book_details:
            del BookManage.book_details[id]
            print("Book deleted successfully")
        else:
            print("Book not found or could not delete book..")

    def showBook():
        if not BookManage.book_details:
            print("No books found..")
            return
        print("\n===== Book List =====")
        print("{:<10}{:<15}{:<12}{:<15}".format("ID", "Name", "Price", "Author"))
        print("-" * 50)
        for book in BookManage.book_details.values():
            print("{:<10}{:<15}{:<12}{:<15}".format(book.bid, book.bname, book.price, book.author))
    def searchBook():
        id = input("Enter book id to search: ")
        if id in BookManage.book_details:
            print("Book  Found:", BookManage.book_details[id])
        else:
            print("Book not found.")