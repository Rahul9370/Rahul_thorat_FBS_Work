"""6. Python Program to Take in a String and Replace Every Blank Space
with Hyphen"""

mystr = "rahul shahu thorat"
print(mystr.replace(" ","-"))

# or using join method
mystr = "rahul   shahu   thorat"
print("-".join(mystr.split()))
