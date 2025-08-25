"""3. Create a class Shirt with members as sid,sname,type(formal etc), price and
size(small,large etc) .Add following methods:
j. Constructor (Support both parameterized and parameterless)
k. Destructor
l. ShowShirt
m. For each size of shirt price should change by 10%.
(eg. If 1000 is price then small price = 1000, medium = 1100,large=1200 and
xlarge=1300) Use static concept."""
class Shirt:
    size_price = {
        "S": 1.0,   # 100% = original
        "M": 1.1,   
        "L": 1.2,   
        "XL": 1.3   
    }

    def __init__(self, sid=0, sname="unknown", stype="Formal", price=99, size="M"):
        self.sid = sid
        self.sname = sname
        self.stype = stype
        self.price = price
        self.size = size

    def ShowShirt(self):
        print(" Shirt id :", self.sid,
              "\n Shirt name :", self.sname,
              "\n Shirt type :", self.stype,
              "\n Shirt price :", self.price,
              "\n Shirt size :", self.size)

    def changePrice(self):
        if self.size in Shirt.size_price:
            old_price = self.price
            self.price = int(self.price * Shirt.size_price[self.size])
            print(f"Price updated from {old_price} to {self.price} for size {self.size}")
        else:
            print("Invalid size, no price change applied.")

    def __del__(self):
        print("Destructor called for Shirt id:", self.sid)


p1 = Shirt(1, "Checks", "Kurta", 2000, "XL")
p1.ShowShirt()
p1.changePrice()
