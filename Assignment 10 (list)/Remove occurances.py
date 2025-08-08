"""10. Write a program to remove all occurrences of a given element in the list."""
list1 = [10, 20, 30, 20, 40, 20, 50]
num = 20   # remove number
i = 0
while(i < len(list1)):
    if(num == list1[i]):
        list1.remove(num)
    else:
        i += 1
print(list1)
