# 3. Python Program to Sort the List According to the Second Element in Sublist
list1 = [[1,3],[4,1],[3,2]]

for i in range(len(list1)):
    for j in range(len(list1)-i-1):
        if(list1[j][1] > list1[j+1][1]):
            list1[j],list1[j+1]=list1[j+1],list1[j]
            print(list1)
            
