"""9. Write a Python program to find all the unique combinations of 3
numbers from a given list of numbers, adding up to a target number."""

mylist = [1,2,3,4,5,6,]
target = 10
myset = set()
for i in range(len(mylist)):
    for j in range(i+1,len(mylist)):
        for k in range(j+1,len(mylist)):
            if(target == mylist[i]+mylist[j]+mylist[k]):
                myset.add(tuple(sorted((mylist[i], mylist[j], mylist[k]))))

print("unique combinations of 3 num is :",myset)