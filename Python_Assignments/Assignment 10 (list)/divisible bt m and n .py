# 11. Write a program to print all numbers which are divisible by m and n in the list.

def DivisibleList(mylist,m,n):
    newlist = []
    for i in mylist:
        if i%m==0 and i%n==0:
            newlist.append(i)
    print("Newlist is :",newlist)

mylist = [2,4,12,90,6,7,9,10,15,26,85,76,32,94,65,7,51,55,2,45,70]
m = int(input("Enter a value of m :"))
n = int(input("Enter a value of n :"))
print(mylist)
DivisibleList(mylist,m,n)