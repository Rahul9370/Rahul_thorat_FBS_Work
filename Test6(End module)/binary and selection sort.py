# take list of numbers (unsorted) from user. while searching element use binary search technique and selection sort.
def selection_sort(a):
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
    return a

def binary_search(a, x):
    low = 0
    high = len(a) - 1
    while low <= high:
        mid = (low + high) // 2
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

a = list(map(int, input("Enter numbers: ").split()))
x = int(input("Enter number to search: "))

a = selection_sort(a)
print("Sorted list:", a)

pos = binary_search(a, x)
if pos != -1:
    print("Found at position", pos)
else:
    print("Not found")
