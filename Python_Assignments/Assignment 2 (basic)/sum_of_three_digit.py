# sum of three digit number

num = int(input("Enter a any three digit number:"))

a = num % 10
num = num // 10
b = num % 10
c = num // 10

sum = a + b + c

print("sum of three  digit is: ",sum)