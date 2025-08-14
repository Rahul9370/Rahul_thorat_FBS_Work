"""
7. Given two sets of numbers, write a Python program to find the missing
numbers in the second set as compared to the first and vice versa.
Use the Python set.
"""

set1 = {5,8,6,2,3,9}
set2 = {2,8,4,5,3,1}
missing_num1 = set1 - set2
missing_num2 = set2 - set1
print("This are the missing number of set1 :", missing_num1)
print("This are the missing number of set2 :", missing_num2)
