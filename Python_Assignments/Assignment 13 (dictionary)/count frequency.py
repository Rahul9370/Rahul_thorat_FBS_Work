# 8. Python Program to Count the Frequency of Words Appearing in a String Using a Dictionary
s = "hi Rahul Hello Rahul Hello bhai"
w = s.split()
d = {}

for x in w:
    if x in d:
        d[x] += 1
    else:
        d[x] = 1

print(d)
