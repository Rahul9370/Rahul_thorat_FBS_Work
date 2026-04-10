"""1. Develop a simple calculator program that performs basic arithmetic operations (+,
-, *, /) on two numbers provided by the user. The program should ask the user for
the numbers and the operator. However, the program should handle the following
exceptions:
a. Invalid Number: If the user enters a number that is not valid, catch the
exception and display an error message.
b. Invalid Operator: If the user enters an operator other than "+", "-", "*", or
"/", catch the exception and display an error message.
c. Division by Zero: If the user tries to divide by zero, catch the exception and
display an error message.
Write a program that performs the requested arithmetic operation and
handles the exceptions as described above."""
try:
    print("Calculator")
    num1 = int(input("Enter number 1 : "))
    num2 = int(input("Enter number 2 : "))
    option = input("Enter operator (+, -, *, /): ")

    if option == "+":
        print("Addition:", num1 + num2)
    elif option == "-":
        print("Subtraction:", num1 - num2)
    elif option == "*":
        print("Multiplication:", num1 * num2)
    elif option == "/":
        try:
            print("Division:", num1 / num2)
        except ZeroDivisionError:
            print("Error: Cannot divide by zero")
    else:
        print("Invalid Operator entered")

except ValueError:
    print("Error: Please enter valid integers only")
