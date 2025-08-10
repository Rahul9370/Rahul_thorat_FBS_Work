# 12. Python Program to count number of lowercase characters in a string.
mystr = "RahulThorat"
c = 0

for ch in mystr:
    if 'a' <= ch <= 'z':  # lowercase check
        c += 1

print("Number of lowercase characters:", c)
