# 4. Python Program to Find the Second Largest Number in a List Using Bubble Sort
list1 = [97, 45, 63, 98, 12, 74, 36]
secLargest = 0
max = list1[0]

print("Original List:", list1)

for i in range(len(list1)):
    for j in range(len(list1) - i - 1):
        if list1[j] > list1[j + 1]:  
            list1[j], list1[j + 1] = list1[j + 1], list1[j]

max = list1[-1]
secLargest = list1[-2]

print("Sorted list using Bubble sort:", list1)
print("Second Largest Element is:", secLargest)

