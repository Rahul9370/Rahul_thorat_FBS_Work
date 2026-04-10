# 1. Find all of the numbers from 1–1000 that are divisible by 8

nums = (x for x in range(1, 1001) if x % 8 == 0)

# print all numbers
for num in nums:
    print(num)

# using list
# Using list comprehension
divisible_by_8 = [n for n in range(1, 1001) if n % 8 == 0]

print(divisible_by_8)

