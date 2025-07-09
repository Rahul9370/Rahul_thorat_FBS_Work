# 6. WAP to check if a given number is prime number or not.

number = int(input("Enter a number to find given number is prime or not prime : "))

for i in range(2, number):
    if(number % i == 0):
        print(number, "is not a prime number.")
        break
else:
    print(number, "is a prime number.")
    