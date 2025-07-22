'''  9. Write a program to check if entered number is a palindrome or not
'''
def Palindrome(num):
    original_number = num
    rev=0
    while(num != 0):
        digit = num % 10
        rev = rev*10 + digit
        num = num // 10
    if(original_number == rev):
        print(original_number,"is palindrome number")
    else:
        print(original_number,"is not palindrome number")
        


num = int(input("Enter number to check number is palindrome or not :"))

Palindrome(num)