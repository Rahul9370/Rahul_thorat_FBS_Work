# 2. WAP to print all odd numbers until n.

start = int(input("Enter starting number :"))
stop = int(input("Enter stopping number :"))

for x in range(start , stop+1):
    if(x % 2 == 1):
        print("Odd numbers :",x)
    

