# 9. Write a program to create three lists of numbers, their squares and cubes

def SquareCube(list1):
    square = []
    cube = []
    for i in range(len(list1)):
        square.append(list1[i] ** 2)
        cube.append(list1[i] ** 3)
    
    print("Square of number list :", square)
    print("Cube   of number list :", cube)

list1 = []
length = int(input("Enter length of list :"))
print("Enter", length, "numbers in the list :")
for i in range(length):
    element = int(input())
    list1.append(element)

print("Original list :", list1)
SquareCube(list1)
