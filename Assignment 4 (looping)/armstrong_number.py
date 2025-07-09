# 12. WAP to print Armstrong number within a given range

number = int(input("Enter Number :"))
original_number = number
count = 0
sum = 0

while(number > 0):
    number = number // 10
    count += 1

number = original_number

while(number > 0):
    a = number % 10
    number = number // 10
    sum = sum + (a**count)

number = original_number

if(sum == number):
    print("Armstrong number")
else:
    print("Not Armstrong number")

