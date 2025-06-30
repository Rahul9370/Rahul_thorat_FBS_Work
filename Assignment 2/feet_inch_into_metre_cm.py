# 3. Convert distant given in feet and inches into meter and centimeter.

feet = int(input("Enter distance of Feet:"))
inch = int(input("Enter distance of Inches:"))

meter = feet * 0.3048
centimeter = inch * 2.54

print("Feet   into    Meter:",meter)
print("Inch into Centimeter:",centimeter)