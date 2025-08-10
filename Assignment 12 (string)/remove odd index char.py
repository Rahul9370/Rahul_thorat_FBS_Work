"""8. Python Program to Remove the Characters of Odd Index Values in a
String"""
mystr = "rahulthorat"
newstr = ""
for s in range(len(mystr)):
    if(s%2==0):
        newstr += mystr[s]

print("After removing odd Index values in string :",newstr)
