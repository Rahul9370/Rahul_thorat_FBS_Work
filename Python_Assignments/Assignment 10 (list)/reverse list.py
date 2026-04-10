# WAP to reverse the list
list1 = [10,20,30,40,50,60]
list2 = []
for i in range(len(list1)-1,-1,-1):
    list2.append(list1[i])
print(list2)
    