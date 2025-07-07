# WAP to accept year from user and check if it is a leap year or not.

year = int(input("Enter Year :"))

if(year % 4 == 0):
    if(year % 100 == 0):
        if(year % 400 == 0):
            print("Leap Year")
        else:
            print("NOT a Leap Year")
    else:
        print("Leap Year")
else:
    print("NOT a Leap Year")
