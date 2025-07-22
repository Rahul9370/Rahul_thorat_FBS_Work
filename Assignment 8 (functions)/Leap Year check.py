'''  10. Write a program to check if entered year is a leap year or not.
'''
def LeapYear(year):
    if(year % 4 == 0):
        if(year % 100 == 0):
            if(year % 400 == 0):
                print(year,"is Leap Year")
            else:
                print(year,"is NOT a Leap Year")
        else:
            print(year,"is Leap Year")
    else:
        print(year,"is NOT a Leap Year")
        


year = int(input("Enter year to check leap year or not :"))

LeapYear(year)