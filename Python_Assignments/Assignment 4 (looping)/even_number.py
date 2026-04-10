# 1. WAP to print all even numbers until n.

start = int(input("Enter starting number :"))
stop = int(input("Enter stopping number :"))

for x in range(start , stop+1):
    if(x % 2 == 0):
        print("Even numbers :",x)
    

