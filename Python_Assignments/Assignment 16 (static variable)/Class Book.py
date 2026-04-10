"""1. Create a class Book with members as bid,bname,price and author.Add following
methods:
a. Constructor (Support both parameterized and parameterless)
b. Destructor
c. ShowBook
d. Add static variable count and also maintain count of objects created."""

class Book:
    count = 0
    def __init__(self, bid=101, bname="India is a country", price=299, author="xyz"):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author
        Book.count +=1

    def __del__(self):
        print("Destructor")

    def Showbook(self):
        print(f"\nbid :{self.bid}\nbname :{self.bname}\nprice :{self.price}\nauthor:{self.author}\nTotal Books Object :{Book.count}")

b1 = Book(11,"Mi Marathi",499,"Rahul")
b2 = Book(12,"I am Marathi",699,"Rohit")
b3 = Book()
b1.Showbook()
b2.Showbook()
b3.Showbook()