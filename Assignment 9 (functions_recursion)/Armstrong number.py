# WAP to check if given number is armstrong number or not using function recursion
def CountDigit(num):
    if(num==0):
        return 0
    else:
        return 1+CountDigit(num//10)

def ArmstrongSum(num,power):
    if(num == 0):
        return 0
    else:
        digit = num % 10
        return (digit ** power) + ArmstrongSum(num//10 , power)

def Armstrong(num):
    power = CountDigit(num)
    return num == ArmstrongSum(num,power)


num = int(input("Enter number to check given number is armstrong nubmer or not :"))
if Armstrong(num):
    print(num,"is an armstrong number")
else:
    print(num,"is an not armstrong number")