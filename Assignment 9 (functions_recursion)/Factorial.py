# WAP to find factorial using recursion
def Factorial(n):
    if(n==1):
        return 1
    else:
        return n*Factorial(n-1)
    
num = int(input("Enter number to find factorial of that number :"))
fact = Factorial(num)
print("Factorial of",num,"is :",fact)