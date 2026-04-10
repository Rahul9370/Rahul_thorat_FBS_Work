# 4. Sum of all odd numbers between 1 to n

# type-2 
# Passing argument without return value

def SumOfOddNum(num):
    sum=0
    for i in range(1,num+1):
        if(i%2==1):
            sum = sum + i
    print("Sum of 1 to",num,"odd number is :",sum)


num = int(input("Enter number to calculate sum of odd numbers till that number :"))
SumOfOddNum(num)