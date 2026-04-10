# 2. Write a program to find maximum and minimum element in a list.

list1 = [10,50,48,65,87,25,31]
small = list1[0]
max = list1[0]
for i in range(1,len(list1)):
    if(small > list1[i]):
        small = list1[i]
    if(max < list1[i]):
        max = list1[i]
print("Minimum number is :",small)
print("Maximum number is :",max)