"""9. Python Program to Calculate the Number of Words and the Number of
Characters Present in a String"""
mystr = "Rahul Shahu Thorat"

c = 0   # characters
d = 0   # spaces

for s in mystr:
    if s != " ":
        c = c + 1
    else:
        d = d + 1

words = d + 1   # main correction

print("Number of character present in a string is :", c)
print("Number of words     present in a string is :", words)

 


# or using split method
# mystr = "Rahul Shahu Thorat"
# words = len(mystr.split())
# chars = len(mystr.replace(" ", ""))

# print("Number of characters present in string:", chars)
# print("Number of words     present in string:", words)
