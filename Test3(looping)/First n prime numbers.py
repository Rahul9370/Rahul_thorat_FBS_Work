# Write a program to print first n prime numbers


num = int(input("Enter Number to print prime number upto given number:"))

print("Following is the prime numbers upto :",num)

for i in range(2,num+1):
    count = 0
    for j in range(1,i+1):
        if(i % j == 0):
            count += 1
    if(count==2):
        print(i)