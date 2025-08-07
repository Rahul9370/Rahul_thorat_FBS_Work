# WAP to find factorial of all number in given range using recursion

def Factorial(num):
    if(num==1 or num==0):
        return 1
    else:   
        return num*Factorial(num-1)
         

num = int(input("Enter number to find Factorials upto given number :"))

for i in range(1,num+1):
    result = Factorial(i)
    print(result)