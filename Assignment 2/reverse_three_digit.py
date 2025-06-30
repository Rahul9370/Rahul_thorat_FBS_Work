# reverse of three digit number

num = int(input("Enter a any three digit number:"))

a = num % 10
num = num // 10
b = num % 10

reverse = a*10 + b

c = num // 10

reverse = reverse*10 + c

print("sum of three  digit is: ",reverse)