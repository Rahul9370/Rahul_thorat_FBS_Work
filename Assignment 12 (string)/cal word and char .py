"""9. Python Program to Calculate the Number of Words and the Number of
Characters Present in a String"""
# mystr = "Rahul Shahu Thorat"
# c = 0       # for charcters
# d = 1       # for words
# for s in mystr:
#     if(s != " "):
#         c = c + 1
#     else:
#         d = d + 1


# print("Number of character present in a string is :",c)
# print("Number of words     present in a string is :",d)


# or using split method
mystr = "Rahul Shahu Thorat"
words = len(mystr.split())
chars = len(mystr.replace(" ", ""))

print("Number of characters present in string:", chars)
print("Number of words     present in string:", words)
