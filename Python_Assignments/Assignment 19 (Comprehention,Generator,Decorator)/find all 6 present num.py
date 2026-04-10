# 2. Find all of the numbers from 1–1000 that have a 6 in them

num = (x for x in range(1,1001) if '6' in str(x))
for i in num:
    print(i)

# using list
present_6 = [n for n in range(1, 1001) if '6' in str(n)]

print(present_6)