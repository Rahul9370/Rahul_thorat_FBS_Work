# 15. Python Program to find larger string without using built-in functions.
str1 = "rahul"
str2 = "thorat"
c1 = 0
c2 = 0
for s in str1:
    c1 += 1
for s in str2:
    c2 += 1
if(c1 > c2):
    print("Str1 is larger string :",str1)
elif(c2 > c1):
    print("Str2 is larger string :",str2)
else:
    print("both string is equal")
