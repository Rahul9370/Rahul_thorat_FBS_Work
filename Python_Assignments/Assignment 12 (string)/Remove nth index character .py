# 2. Python Program to Remove the nth Index Character from a Non-Empty String

mystr = "Rahulshahuthorat"
print("Original string :",mystr)
n = int(input("Enter any integer number to remove character from string :"))
 
newmystr = mystr[:n] + mystr[n+1:]
print("After removing nth character from string :",newmystr)