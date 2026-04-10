# 7. Write a program to create a new list from existing list which contains cube of
# each number of list.
def cube_elements(list1):
    result = []
    for i in list1:
        result.append(i ** 3)
    return result

list1 = [2, 8, 3, 4, 6, 7]
list2 = cube_elements(list1)
print("Cubed List:", list2)
