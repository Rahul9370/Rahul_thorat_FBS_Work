# write a program to solve following series:
# a. 1!+2!+3!+4!+5!+.....+n!
# b. N + N^2 + N^3 + N^4 +.....N^N (here ^ means exponent)
# c. Find the sum of geometric series from 1 to n where the common ratio is 2.
# d. S = a + a2 / 2 + a3 / 3 +....... + a10 / 10
# e. x - x2/3 + x3/5 - x4/7 + ......to n terms 

# a. 1!+2!+3!+4!+5!+.....+n!
# n = int(input("Enter the value of n: "))
# sum = 0

# for i in range(1, n+1):
#     fact = 1
#     for j in range(1, i+1):
#         fact *= j
#     sum += fact

# print("Sum of factorial series is:", sum)


# b. N + N^2 + N^3 + N^4 +.....N^N (here ^ means exponent)
# N = int(input("Enter value of N: "))
# sum = 0

# for i in range(1, N+1):
#     power = 1
#     for j in range(i):
#         power *= N
#     sum += power

# print("Sum of series N + N^2 + ... + N^N is:", sum)


# c. Find the sum of geometric series from 1 to n where the common ratio is 2.
# n = int(input("Enter number of terms: "))
# sum = 0
# term = 1  # first term

# for i in range(n):
#     sum += term
#     term *= 2

# print("Sum of geometric series is:", sum)


# d. S = a + a2 / 2 + a3 / 3 +....... + a10 / 10
# a = int(input("Enter value of a: "))
# sum = 0.0

# for i in range(1, 11):
#     power = 1
#     for j in range(i):
#         power *= a
#     sum += power / i

# print("Sum of the series is:", sum)


# e. x - x2/3 + x3/5 - x4/7 + ......to n terms 
# x = int(input("Enter value of x: "))
# n = int(input("Enter number of terms: "))
# sum = 0.0
# sign = 1
# denominator = 1

# for i in range(1, n+1):
#     power = 1
#     for j in range(i):
#         power *= x
#     sum += sign * (power / denominator)
#     sign *= -1
#     denominator += 2

# print("Sum of the series is:", sum)

