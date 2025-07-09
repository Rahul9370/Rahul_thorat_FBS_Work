# 8. WAP to find which numbers are divisible by 7 and multiple of 5 in a given range.

number = int(input("Enter number :"))

for i in range(5 , number+1):
    if(i % 7 == 0 and i % 5 == 0):
        print(i)