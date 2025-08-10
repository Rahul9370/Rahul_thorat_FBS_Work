"""4. Python Program to Form a New String where the First Character and
the Last Character have been Exchanged"""
# rahul == lahur
string1 = "rahul"
first = string1[0]
middle = string1[1:-1]
last = string1[-1]
newstr = last + middle + first
print(newstr)