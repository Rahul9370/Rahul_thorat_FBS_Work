# 3. Write a program to input angles of a triangle and check whether triangle is valid or not.

angle1 = int(input("Enter First Angle of Triangle :"))
angle2 = int(input("Enter Second Angle of Triangle :"))
angle3 = int(input("Enter Third Angle of Triangle :"))

angle_sum = angle1 + angle2 + angle3

if(angle_sum == 180):
    print("Valid Triangle...")
else:
    print("Invalid Triangle...")

