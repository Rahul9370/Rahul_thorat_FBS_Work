"""1. Python Program to Put Even and Odd elements of a List into two Different
Lists"""
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

list1 = [1,2,3,4,5,6,7,8,9]
 
print("Original list:", list1)
EvenOdd(list1)