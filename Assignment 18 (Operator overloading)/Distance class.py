"""2. Create a class Distance with data members as km,m and cm and add following
methods :
a. Constructor
b. Destructor
c. Overload +,- operator"""

class Distance:
    def __init__(self, km=0, m=0, cm=0):
        self.km = km
        self.m = m
        self.cm = cm
        print(f"Constructor called: {self.km}km {self.m}m {self.cm}cm")

    def __del__(self):
        print(f"Destructor called for {self.km}km {self.m}m {self.cm}cm")

    def __str__(self):
        return f"{self.km}km {self.m}m {self.cm}cm"

    def __add__(self, other):
        return Distance(self.km + other.km, self.m + other.m, self.cm + other.cm)

    def __sub__(self, other):
        return Distance(self.km - other.km, self.m - other.m, self.cm - other.cm)


d1 = Distance(2, 900, 80)
d2 = Distance(1, 200, 50)

print("d1:", d1)
print("d2:", d2)

d3 = d1 + d2   # calls __add__
print("Addition:", d3)

d4 = d1 - d2   # calls __sub__
print("Subtraction:", d4)
