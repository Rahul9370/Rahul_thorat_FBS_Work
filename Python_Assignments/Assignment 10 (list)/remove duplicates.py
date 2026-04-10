# WAP to remove Duplicate from the list

# directly converting list into set method
# list1 = [10, 20, 50, 20, 15, 48, 10, 28, 10]  
# set1 = set(list1)
# list1 = list(set1)
# print(list1)

# only use list method to remove duplicate element from the list
list1 = [10, 20, 50, 20, 15, 48, 10, 28, 10]
list2 = []
for i in range(len(list1)):
    if list1[i] not in list2:
        list2.append(list1[i])
print(list2)

# or
# list1 = [10, 20, 50, 20, 15, 48, 10, 28, 10]    
# list2 = []
# for item in list1:
#     if item not in list2:
#         list2.append(item)
# print(list2)

