# WAP to calculate the sum of following series where n is input by user.
# 1/1! + 2/2! + 3/3! + 4/4! + ....N/N!

def Factorial(num):
    sum = 0
    for i in range(1,num+1):
        fact = 1
        for j in range(1,i+1):
            fact =  fact * j
        sum = sum + (i/fact)
    print("Sum of Factorial series like 1/1!+2/2!+... of 1 to",num,"is :",sum)
    
num = int(input("Enter number to find factorials series like 1/1!+2/2!+... upto given number :"))
Factorial(num)