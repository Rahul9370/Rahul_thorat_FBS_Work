# 8. Write a program to create a duplicate of an existing list. It should not point to
# same list.
list1 = [10,20,30,40,50]
list2 = []
for i in list1:
    list2.append(i)
# list1[0] = 55
# list2[0] = 65
print(list1)
print(list2)
# or
print(list1 is list2)  # Output: False
