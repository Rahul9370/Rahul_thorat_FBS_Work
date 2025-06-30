# reverse a two digit number

num = int(input("Enter a any two digit number:"))

a = num // 10
b = num %  10

c = b*10+a

print("After reversing a digit is: ",c)