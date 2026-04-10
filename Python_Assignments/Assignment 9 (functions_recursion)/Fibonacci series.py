# WAP to print fibonacci series using recursion
def Fibonacci(a,b,n):
    if n > 0:
        c= a+b
        print(c)
        Fibonacci(b,c,n-1)


terms = int(input("Enter number of terms in Fibonacci series: "))
a=-1
b=1
print("Fibonacci series:") 
Fibonacci(a,b,terms)
