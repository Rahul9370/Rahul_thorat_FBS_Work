#1. Write a program to calculate area of circle

# type-2 
# Passing argument without return value

def AreaOfCircle(radius):
    area = 3.14 * radius * radius
    print("Area of Circle is :",area)

radius = int(input("Enter radius of circle :"))

AreaOfCircle(radius)