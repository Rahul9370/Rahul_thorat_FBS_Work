"""5. Python Program to Find the Union of two Lists without
using set concept."""

def unionlist(list1,list2):
    newlist = []
    for num in list1:
        if num not in newlist:
            newlist.append(num)
    for num in list2:
        if num not in newlist:
            newlist.append(num)
    
    print(newlist)                # [1, 8, 5, 4, 7, 3, 6, 9, 2]

list1 = [1,2,3,4,5]
list2 = [1,6,7,3,8,9]

unionlist(list1,list2)