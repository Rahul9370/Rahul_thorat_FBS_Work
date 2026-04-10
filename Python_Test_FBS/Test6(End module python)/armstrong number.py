
num = int(input("enter number:"))
count = 0
sum = 0
temp = num
original = num
while(num > 0):
    digit = num % 10
    count += 1
    num = num // 10

while(temp > 0):
    digit = temp % 10
    sum = sum + (digit ** count)
    temp = temp // 10
    
if(original == sum):
    print("Number is Armstrong number...")
else:
    print("Number is not Armstrong number...") 