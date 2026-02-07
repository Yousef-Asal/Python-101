
class book:
    def __init__(self, title, author, stock):
        self.title = title
        self.author = author
        self.stock = stock

    @property
    def stock(self):
        return self.my_stock
    
    @stock.setter
    def stock(self, new_val):
        if new_val < 0:
            raise ValueError("Can't assign a negative value to stock")
        self.my_stock = new_val
        
    def __str__(self):
        return f"Description:\n - Title: {self.title}\n - Author: {self.author}\n - Stock: {self.stock}"
    
    def __eq__(self, value):
        if self.title == value.title and self.author == value.author:
            return True
        return False
    
    def __add__(self,b):
        return self.stock + b.stock
    
    def sell_book(self,quantity):
        self.stock -= quantity


book1 = book("To Kill a Mockingbird","Harber Lee", 7)
book2 = book("To Kill a Mockingbird","Harber Lee", 3)
book3 = book("Moby Dick","Herman Melville", 11)

print(book1,book2,book3,sep='\n')

if book1 == book2:
    print(f"book1 is equal to book2 and the total stock is: {book1+book2}")
if book2 == book3:
    print(f"book2 is equal to book3 and the total stock is: {book2+book3}")
if book1 == book3:
    print(f"book1 is equal to book3 and the total stock is: {book1+book3}")

print(f"book3 stock is: {book3.stock}")
book3.sell_book(6)
print(f"book3 stock is: {book3.stock}")
book3.sell_book(12)
print(f"book3 stock is: {book3.stock}")
