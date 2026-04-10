# 5. Sum of all prime numbers between 1 to n

# type-2 
# Passing argument without return value

def SumOfPrimeNum(num):
    sum=0
    for i in range(2,num+1):
        count=0
        for j in range(1,i+1):
            if(i%j==0):
                count = count+1
        if(count==2):
            sum = sum + i
    print("Sum of 1 to",num,"prime number is :",sum)


num = int(input("Enter number to calculate sum of prime numbers till that number :"))
SumOfPrimeNum(num)