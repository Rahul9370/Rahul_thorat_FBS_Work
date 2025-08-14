"""1. Write a Python program to find elements in a given set that are not in
another set."""
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}

result = set1 - set2   # set difference

print("Elements in set1 not in set2:", result)
