#1. Convert the time entered in hh,min and sec into seconds.

hour = int(input("Enter hour:"))
minute = int(input("Enter minute:"))
second = int(input("Enter second:"))

seconds = hour * 3600 + minute * 60 + second

print("After converting hour,min and sec into seconds:",seconds)
