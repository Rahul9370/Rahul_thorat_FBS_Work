# sum of two digit number

num = int(input("Enter a any two digit number:"))

a = num // 10
b = num %  10

a += b

print("sum of two  digit is: ",a)