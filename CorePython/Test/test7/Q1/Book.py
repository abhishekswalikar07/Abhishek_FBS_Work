class Book:
    def __init__(self,bid,bname,price,author):
        self.bid=bid
        self.bname=bname
        self.price=price
        self.author=author
    
    def __str__(self):
        return f'{self.bid}, {self.bname}, {self.price}, {self.author}'