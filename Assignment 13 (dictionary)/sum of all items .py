# 5. Python Program to Sum All the Items in a Dictionary
d = {"a": 10, "b": 20, "c": 30}
s = 0

for v in d.values():
    s += v

print("Sum is:", s)
