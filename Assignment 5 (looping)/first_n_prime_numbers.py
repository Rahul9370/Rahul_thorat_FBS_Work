# 7. write a program to print first n prime numbers 

n = int(input("Enter how many prime numbers you want: "))
count = 0      # To count how many prime numbers printed
num = 2        # Starting number to check

while count < n:
    divisor_count = 0

    for i in range(1, num):  # Check how many numbers divide num
        if num % i == 0:
            divisor_count += 1

    if divisor_count == 1:   
        print(num, end=" ")
        count += 1           # Increase count when a prime is found
    num += 1   # Go to next number

