# WAP to calculate the n to the power n using recursion
def Power(base, power):
    if power == 0:
        return 1
    else:
        return base * Power(base, power - 1)

n = int(input("Enter number to calculate n^n: "))
result = Power(n, n)

print(n, "^", n, "=", result)
