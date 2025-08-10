# 5. Python Program to Sort a List According to the Length of the Elements within the list.

mylist = ["rahul", "roshan", "om", "sudarshan"]

# Bubble sort according to length
for i in range(len(mylist)):
    for j in range(len(mylist) - i - 1):
        if len(mylist[j]) > len(mylist[j + 1]):
            mylist[j], mylist[j + 1] = mylist[j + 1], mylist[j]

print("Sorted list according to length:", mylist)



# or using sort method directly 
# mylist = ["rahul","roshan","om","sudarshan"]

# mylist.sort(key=len)  

# print("Sorted list according to length:", mylist)
