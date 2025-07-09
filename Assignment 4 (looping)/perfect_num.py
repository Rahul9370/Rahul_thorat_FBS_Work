# 10. WAP to check if given number is Perfect Number.

number = int(input("Enter number :"))
total = 0

for i in range(1 , number):
    if(number % i == 0):
        total = total + i
        if(total == number):
            print(number,"is perfect number")
            break
else:
    print(number,"is NOT perfect number")