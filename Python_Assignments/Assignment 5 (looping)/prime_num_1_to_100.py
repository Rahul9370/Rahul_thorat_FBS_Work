# 6. Write a program to print prime numbers between 1 to 100.

for i in range(2 , 101):
    count = 0
    for j in range(1 , i):
        if(i % j == 0):
            count += 1
    if(count == 1):
        print(i)