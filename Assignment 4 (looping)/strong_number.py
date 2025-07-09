# 11. WAP to check if given number Strong Number.

number = int(input("Enter number to check Armstrong number :"))

original_num = number
sum = 0

while(number > 0):
    a = number % 10
    factorial = 1
    for i in range(1 , a+1):
        factorial *= i

    sum += factorial
    number //= 10 

if(sum == original_num):
    print("Armstrong number")
else:
    print("Not Armstrong number")






# num = int(input("Enter a number: "))
# original = num
# sum = 0

# while num > 0:
#     digit = num % 10

#     # Factorial calculate karna manually
#     fact = 1
#     i = 1
#     while i <= digit:
#         fact = fact * i
#         i = i + 1

#     sum = sum + fact
#     num = num // 10

# if sum == original:
#     print(original, "is a Strong Number")
# else:
#     print(original, "is not a Strong Number")
