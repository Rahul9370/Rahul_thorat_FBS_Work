"""3. Create a class Shirt with members as sid,sname,stype(formal etc), price and
size(small,large etc) .Add following methods:
g. Constructor (Support both parameterized and parameterless)
h. Destructor
i. ShowShirt"""
class Shirt:
    def __init__(self,sid=0, sname="unknown", stype="Formal", price=99, size="xl"):
        self.sid = sid
        self.sname = sname
        self.stype = stype
        self.price = price
        self.size = size
    
    def ShowShirt(self):
        print(" Shirt id :",self.sid,"\n","Shirt name :",self.sname,"\n","Shirt type :",self.stype,"\n","Shirt price :",self.price,"\n","Shirt size :",self.size)

    def __del__(self):
        print("Destructor")

p1 = Shirt(1,"Checks","kurta",2000,"XXL")

p1.ShowShirt()