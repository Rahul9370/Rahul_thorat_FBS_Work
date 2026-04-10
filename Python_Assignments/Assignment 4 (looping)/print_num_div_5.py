# 9. WAP to print all numbers in a range divisible by a given number.

start = int(input("Range Start number :"))
stop = int(input("Range Stop number :"))
divisor = int(input("Enter divisor number :"))

for i in range(start , stop+1):
    if(i % divisor == 0):
        print(i)