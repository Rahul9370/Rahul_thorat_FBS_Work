# WAP to print Fibonacci series up to a given number.

number = int(input("Enter a number to print Fibonacci series up to that number: "))

a = 0
b = 1 

for i in range(1 , number+1):
    c = a + b
    print(c)
    a = b 
    b = c