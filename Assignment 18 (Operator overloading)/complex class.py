"""1. Create a class Complex Number with data members as real and imag and add
following methods :
a. Constructor
b. Destructor
c. Overload +,- operator"""

class Complex:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag
        print(f"Constructor called: {self.real}+{self.imag}i")

    def __del__(self):
        print(f"Destructor called for {self.real}+{self.imag}i")

    def __str__(self):
        return f"{self.real}+{self.imag}i"
    

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    
    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)


c1 = Complex(4, 5)
c2 = Complex(2, 3)

print("c1:", c1)
print("c2:", c2)

c3 = c1 + c2   # calls __add__
print("Addition:", c3)

c4 = c1 - c2   # calls __sub__
print("Subtraction:", c4)
