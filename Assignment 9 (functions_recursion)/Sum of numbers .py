# WAP to find sum of n numbers using recursion
def SumOfN(n):
    if n == 0:
        return 0
    else:
        return n + SumOfN(n - 1)

num = int(input("Enter number to find sum from 1 to n: "))
total = SumOfN(num)

print("Sum of numbers from 1 to", num, "is:", total)
