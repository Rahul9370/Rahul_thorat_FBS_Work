# WAP to finf factorial of a given number using for loop.

number = int(input("Enter a number to find factorial: "))

factorial = 1

for i in range(1, number + 1):
    factorial *= i

print("Factorial of", number, "is", factorial)

