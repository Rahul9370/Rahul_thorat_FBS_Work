# 6. Python Program to Find the Union of two Lists
# list1 = [10,40,20,50,60,30]
# list2 = [60,70,40,80,20,90]
# list3 = []

# for item in list1:
#     if item not in list3:
#         list3.append(item)

# for item in list2:
#     if item not in list3:
#         list3.append(item)

# print(list3)


# using set ds
list1 = [10, 40, 20, 50, 60, 30]
list2 = [60, 70, 40, 80, 20, 90]

list3 = list(set(list1) | set(list2))
print(list3)
