"""5. Accept a number from user and check if this element is present in the list or
not. Also tell how many times it is present in the list."""

def PresentElement(list1, num):
    count = 0
    for i in list1:
        if num == i:
            count += 1
    
    if count > 0:
        return f"{num} is present in the list {count} times."
    else:
        return f"{num} is not present in the list."

list1 = [10, 20, 50, 20, 15, 48, 10, 28, 10]
print("Actual list:", list1)
num = int(input("Enter number to check if it's present in the list: "))

result = PresentElement(list1, num)
print(result)
