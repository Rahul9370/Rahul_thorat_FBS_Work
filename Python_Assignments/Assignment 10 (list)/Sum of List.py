# 1. Write a program to find sum of all elements of list

list1 = [10,50,5,48,65]
length = len(list1)
sum = 0
for x in list1:
    sum = sum + x       # traversing by using special variable directly

print("sum of",list1,"is :",sum)