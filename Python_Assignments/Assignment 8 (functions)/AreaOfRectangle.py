#1. Write a program to calculate area of rectangle

# type-2 
# Passing argument without return value

def AreaOfRectangle(length,width):
    area = length * width
    print("Area of Ractangle is :",area)

length = int(input("Enter length of rectangle :"))
width = int(input("Enter width of rectangle :"))

AreaOfRectangle(length,width)