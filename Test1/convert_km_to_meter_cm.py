# WAP to accept distance in km and convert it into  meters and centimeters both.

kilometer = int(input("Enter a Kilometer:"))

meter = 1000 * kilometer
centimeter = 100000 * kilometer

print(kilometer,"is equal to ",meter,"meters")
print(kilometer,"is equal to ",centimeter,"centimeters")