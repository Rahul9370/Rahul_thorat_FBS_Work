# 1. Write a program to find sum of following series using recursive functions:
# i. 1! + 2! + 3! + 4! +..... + n!
# Note : For fact and sum two recursive functions


def Factorial(n):
    if (n == 1):
        return 1
    else:
        return n * Factorial(n - 1)

def SumOfFactorials(n):
    if (n == 1):
        return Factorial(1)
    else:
        return Factorial(n) + SumOfFactorials(n - 1)

num = int(input("Enter number to find sum of factorials up to that number: "))
total = SumOfFactorials(num)
print("Sum of factorials from 1! to", num, "is:", total)
