# 5. Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.

side1 = int(input("Enter side 1 of Triangle :"))
side2 = int(input("Enter side 2 of Triangle :"))
side3 = int(input("Enter side 3 of Triangle :"))

if(side1 == side2 == side3):
    print("Triangle is Equilateral triangle.")
elif(side1 == side2 or side2 == side3 or side1 == side3):
    print("Triangle is Issoscelious triangle.")
else:
    print("Triangle is Scaler triangle.")