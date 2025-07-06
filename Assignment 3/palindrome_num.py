# 12. Write a program to check if given 3 digit number is a palindrome or not.

number = int(input("Enter any Three digit number :"))

temp_number = number
a = temp_number % 10
temp_number = temp_number // 10
b = temp_number % 10

reverse = a*10 + b

c = temp_number // 10

reverse = reverse*10 + c 

if(number == reverse):
    print("Number is Palindrome...")
else:
    print("Number is Not Palindrome...")