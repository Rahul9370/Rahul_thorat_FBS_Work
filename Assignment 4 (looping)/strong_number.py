# 11. WAP to check if given number Strong Number.

number = int(input("Enter number to check Armstrong number :"))

original_num = number
sum = 0

while(number > 0):
    a = number % 10
    number //= 10
    factorial = 1
    for i in range(1 , a+1):
        factorial *= i
    sum += factorial
     
if(sum == original_num):
    print("Armstrong number")
else:
    print("Not Armstrong number")


 
