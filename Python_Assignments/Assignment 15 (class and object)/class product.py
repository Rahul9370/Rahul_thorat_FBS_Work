"""2. Create a class Product with members as pid,pname,price and quantity .Add
following methods:
d. Constructor (Support both parameterized and parameterless)
e. Destructor
f. ShowBook"""
class Product:
    def __init__(self,pid=0, pname="unknown", price=99, quantity=1):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity
    
    def ShowBook(self):
        print("Product id :",self.pid,"\n","Product name :",self.pname,"\n","Product price :",self.price,"\n","Product quantity :",self.quantity)

    def __del__(self):
        print("Destructor")

p1 = Product(1,"watch",599,2)

p1.ShowBook()