# 7. WAP to print all integers upto n that aren’t divisible by 2 and 3.

number = int(input("Enter Number :"))

for i in range(1 , number+1):
    if(i % 2 != 0 and i % 3 != 0):
        print(i)
    