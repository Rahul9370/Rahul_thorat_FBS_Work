# 8. Print 1 to 100 in snakes and ladder pattern.
n = 100
row = 1
ladder = []

for i in range(10):
    temp = []
    for j in range(10):
        temp.append(n)
        n -= 1
    if row % 2 == 0:  
        temp.reverse()
    ladder.append(temp)
    row += 1

for r in ladder:
    print(r)
