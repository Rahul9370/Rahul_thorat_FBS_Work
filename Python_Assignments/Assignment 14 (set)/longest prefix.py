"""5. Write a Python program to find the longest common prefix of all
strings. Use the Python set."""

myset = {"first", "firstb", "firstbi", "firstbit", "firstbitsolutions"}

mylist = list(myset)
shortest = min(myset, key=len)

prefix = ""

for i in range(len(shortest)):
    chars = set()
    for word in mylist:
        chars.add(word[i])
    if len(chars) == 1:
        prefix += shortest[i]
    else:
        break  

print("Longest Common Prefix:", prefix)
