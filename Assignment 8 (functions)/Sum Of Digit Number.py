# 7. Write a program to find sum of digits of a number.

# type-2 
# Passing argument without return value

def SumOfNum(num):
    sum=0
    digit=num
    while(num != 0):
        a = num % 10
        sum = sum + a
        num = num // 10
    print("Sum of",digit,"digits is:",sum)


num = int(input("Enter number to calculate sum of digits :"))
SumOfNum(num)