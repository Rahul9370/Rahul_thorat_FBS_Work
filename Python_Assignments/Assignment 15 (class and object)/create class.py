"""1. Create a class Book with members as bid,bname,price and author.Add following
methods:
a. Constructor (Support both parameterized and parameterless)
b. Destructor
c. ShowBook"""

class Book:
    def __init__(self, bid=101, bname="India is a country", price=299, author="xyz"):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author

    def __del__(self):
        print("Destructor")

    def Showbook(self):
        print(f"bid :{self.bid}\nbname :{self.bname}\nprice :{self.price}\nauthor: {self.author}")

b1 = Book(11,"Mi Marathi",499,"Rahul")
b1.Showbook()