# 6. Python Program to Multiply All the Items in a Dictionary
d = {"a": 2, "b": 3, "c": 4}
m = 1

for v in d.values():
    m *= v

print("Multiplication is:", m)
