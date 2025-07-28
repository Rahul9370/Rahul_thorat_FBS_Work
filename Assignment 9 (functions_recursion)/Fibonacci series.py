# WAP to print fibonacci series using recursion
def Fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)


terms = int(input("Enter number of terms in Fibonacci series: "))

print("Fibonacci series:")
for i in range(terms):
    print(Fibonacci(i), end=" ")
