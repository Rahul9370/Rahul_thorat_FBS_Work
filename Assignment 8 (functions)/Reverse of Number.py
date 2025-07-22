''' 8. Write a program find reverse of a number
'''
def Reverse(num):
    temp = num
    rev=0
    while(num != 0):
        digit = num % 10
        rev = rev*10 + digit
        num = num // 10
    print("reverse of ",temp,"is :",rev)
        


num = int(input("Enter number to reverse number :"))

Reverse(num)