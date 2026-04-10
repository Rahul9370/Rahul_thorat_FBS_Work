 # 12. WAP to print Armstrong numbers within a given range.

start = int(input("Enter starting number of range: "))
stop = int(input("Enter stopping number of range: "))

for i in range(start, stop + 1):
    temp = i
    count = 0
    num = temp
    while num > 0:
        num = num // 10
        count += 1

    num = temp
    sum = 0
    while num > 0:
        digit = num % 10
        sum += digit ** count
        num = num // 10

    if temp == sum:
            print("Armstrong number:", temp)
    
         
