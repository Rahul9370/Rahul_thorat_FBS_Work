# 8. Write a program to swap two numbers using third variable.

number1 = int(input("Enter number 1 is:"))
number2 = int(input("Enter number 2 is:"))

temp = number1
number1 = number2
number2 = temp

print("After swapping number 1 is:",number1)
print("After swapping number 2 is:",number2)