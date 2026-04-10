#2. Python Program to Merge Two Lists and Sort it
list1 = [3, 1, 5]
list2 = [4, 2, 6]
mergeList = []
for i in list1:
    mergeList.append(i)
print("After merging list1 :",mergeList)        # [3, 1, 5]
for i in list2:
    mergeList.append(i)
print("After merging list2 :",mergeList)        # [3, 1, 5, 4, 2, 6]

for j in range(1,len(mergeList)):
    for i in range(len(mergeList)-j):
        if(mergeList[i] > mergeList[i+1]):
            mergeList[i],mergeList[i+1] = mergeList[i+1],mergeList[i]
print("After sorting of merglist :",mergeList)





