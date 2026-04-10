"""2. Create a class Product with members as pid,pname,price and quantity .Add
following methods:
e. Constructor (Support both parameterized and parameterless)
f. Destructor
g. ShowBook
h. Add static member discount.
i. Provide methods for applying discount on price of product."""
class Product:
    discount = 10
    def __init__(self,pid=0, pname="unknown", price=99, quantity=1):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity
    
    def ShowProduct(self):
        print("Product id :",self.pid,"\n","Product name :",self.pname,"\n","Product price :",self.price,"\n","Product quantity :",self.quantity)
        print("After giving Discount price is :",self.calDiscount())
    
    def calDiscount(self):
        Pdiscount = self.price-(self.price * Product.discount)/100
        return Pdiscount

    def __del__(self):
        print("Destructor is called for",self.pname)

p1 = Product(1,"watch",599,2)

p1.ShowProduct()