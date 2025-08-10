# 7. Python Program to Find the Intersection of Two Lists
list1 = [10, 40, 20, 50, 60, 30]
list2 = [60, 70, 40, 80, 20, 90]
intersection_list = []

for item in list1:
    if item in list2 and item not in intersection_list:
        intersection_list.append(item)

print("Intersection:", intersection_list)
