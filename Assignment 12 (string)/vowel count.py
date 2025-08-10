# 5. Python Program to Count the Number of Vowels in a String
mystr = "rahulthorat"
count = 0
for c in mystr:
    if(c == "a" or c == "e" or c == "i" or c == "o" or c == "u"):
        count += 1
print("Vowels in given string is :",count)

# or using in operator directly
# for c in mystr:
#     if c in "aeiou":
#         count += 1
# print("Vowels in given string is :",count)