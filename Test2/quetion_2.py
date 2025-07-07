#
#

number = int(input("Enter any Three digit Number :"))

num3 = number % 10
num = number // 10
num2 = num % 10
num1 = num // 10

if(num2*2 == num1 and num1*2 == num3):
    print("Yes, you have done it !")
else:
    print("Please try next time !")