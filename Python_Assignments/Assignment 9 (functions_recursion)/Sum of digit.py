# WAP to find sum of digit using function recursion
def SumOfDigits(num):
    if(num!=0):
        a = num % 10
        return a + SumOfDigits(num//10)
    else:
        return 0

num = int(input("Enter number to find sum of digits: "))
total = SumOfDigits(num)

print("Sum of digits of", num, "is:", total)
