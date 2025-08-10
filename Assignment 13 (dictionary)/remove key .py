# 7. Python Program to Remove the Given Key from a Dictionary
d = {"name": "Rahul", "age": 22, "city": "Aurangabad"}
k = "age"

if k in d:
    del d[k]

print(d)
