"""4. Write a program to check if given number is Armstrong number or not.
(Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 +
4*4*4*4)"""

number = int(input("Enter number to check Armstrong number or not :"))
original_num = number
num = number
count = 0

while(number > 0):
    number = number // 10
    count += 1

sum = 0
while(num > 0):
    digit = num % 10
    sum += (digit ** count)
    num = num // 10
    
if(original_num == sum):
    print("Entered number is Armstrong number.")
else:
    print("Entered number is Not Armstrong number.")


