# # 3. Write a program to find the second largest element in the list.

list1 = [10,50,48,65,87,25,31]
max = list1[0]
sec_max = 0
for i in range(1,len(list1)):
    if(max < list1[i]):
        sec_max = max
        max = list1[i]
print("Second Maximum number is :",sec_max)
