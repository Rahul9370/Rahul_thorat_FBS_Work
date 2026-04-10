'''
6. Write a program to find print the following Fibonacci series using
functions:
1 1 2 3 5 8 n terms
'''
def Fibonacci(num):
    a=0
    b=1
    print("Fibonacci series is upto ",num,"th term is :")
    print(b)
    for i in range(1,num):
        c = a + b
        print(c)
        a = b 
        b = c


num = int(input("Enter number to print fibonacci series upto entered numbers term :"))

Fibonacci(num)