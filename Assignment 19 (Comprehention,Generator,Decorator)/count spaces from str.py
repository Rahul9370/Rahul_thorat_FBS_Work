# 3. Count the number of spaces in a string (take input from user)

mystring = input("Enter string :")
spaces = sum(1 for x in mystring if x == " ")
print("Total Spaces in s string is :",spaces)