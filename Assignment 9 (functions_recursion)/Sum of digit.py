# WAP to find sum of digit using function recursion
def SumOfDigits(num):
    if num == 0:
        return 0
    else:
        return (num % 10) + SumOfDigits(num // 10)

num = int(input("Enter number to find sum of digits: "))
total = SumOfDigits(num)

print("Sum of digits of", num, "is:", total)
