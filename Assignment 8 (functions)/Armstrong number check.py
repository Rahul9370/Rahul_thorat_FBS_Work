'''11. WAP to check if a given number is Armstrong number or not. For
each task create separate functions.'''
"""
(Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 +
4*4*4*4)"""

 
def Count(number):          # to check digits in number for multiplying each digit is count time
    count = 0
    while(number > 0):
        number = number // 10
        count += 1
    return count
 
def Sum(power,number):      # to multiply each digit with power and addition of multiplication
    sum = 0
    while(number > 0):
        digit = number % 10
        sum += (digit ** power)
        number = number // 10
    return sum
     
def ArmstrongNumber(number,result):   # to check given number is armstrong or not
    if(number == result):
        print("Entered number is Armstrong number.")
    else:
        print("Entered number is Not Armstrong number.")


number = int(input("Enter number to check Armstrong number or not :"))
power = Count(number)
result = Sum(power,number)
ArmstrongNumber(number,result)



