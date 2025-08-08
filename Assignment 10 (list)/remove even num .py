# 13 . Write a program to print list after removing even numbers.
# mylist = [10, 85, 54, 77, 62, 74, 63, 57, 69]
# print("Original List is :", mylist)

# newlist = []
# for i in mylist:
#     if i % 2 != 0:
#         newlist.append(i)

# print("After removing even numbers :", newlist)

# or

mylist = [10, 85, 54, 77, 62, 74, 63, 57, 69]
for i in mylist[:]:   # iterate over copy
    if i % 2 == 0:
        mylist.remove(i)
print(mylist)
