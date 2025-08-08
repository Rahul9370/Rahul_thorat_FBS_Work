"""9. Write a program of having n number of elements in the list and find out even
and odd elements in that list and then create two separate lists which will have
even elements and other will have odd elements."""

# def EvenOdd(list1):
#     even = []
#     odd = []
#     for i in range(len(list1)):
#         if(list1[i]%2==0):
#             even.append(list1[i])
#         else:
#             odd.append(list1[i])
    
#     print("Even number list :",even)
#     print("Odd  number list :",odd)

# list1 = []
# length = int(input("Enter length of list :"))
# print("Enter",length,"elements in the list :")
# for i in range(length):
#     element = int(input())
#     list1.append(element)

# print("Original list :",list1)
# EvenOdd(list1)

# or
def EvenOdd(list1):
    even = []
    odd = []
    for num in list1:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    
    print("Even number list :", even)
    print("Odd  number list :", odd)

list1 = []
length = int(input("Enter length of list: "))
print("Enter", length, "elements in the list:")
for _ in range(length):
    element = int(input())
    list1.append(element)

print("Original list:", list1)
EvenOdd(list1)
