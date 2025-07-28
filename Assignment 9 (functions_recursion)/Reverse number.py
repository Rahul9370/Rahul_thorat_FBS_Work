# WAP to reverse a given number using function recursion
def ReverseNumber(num, rev=0):
    if num == 0:
        return rev
    else:
        digit = num % 10
        rev = rev * 10 + digit
        return ReverseNumber(num // 10, rev)

num = int(input("Enter number to reverse: "))
reversed_num = ReverseNumber(num)

print("Reversed number is:", reversed_num)
