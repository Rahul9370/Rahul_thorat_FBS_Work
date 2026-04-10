# 13. Python Program to count number of digits and letters in a string.
mystr = "Rahul 1234"
char = 0
digit = 0
for i in mystr:
    if(i.isalpha()):
        char += 1
    elif(i.isdigit()):
        digit += 1

print("Total character in string :",char)
print("Total  digit    in string :",digit)
