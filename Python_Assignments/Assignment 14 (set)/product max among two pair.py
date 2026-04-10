"""
6. Write a Python program to find the two numbers whose product is
maximum among all the pairs in a given list of numbers. Use the
Python set.
"""
myset = {4,5,2,3,7,1}
mylist = list(myset)
ans = 0
num1 = 0
num2 = 0
for i in range(len(mylist)):
    product = 0
    for j in range(i+1,len(mylist)):
        product = mylist[i]*mylist[j]
        if(ans < product):
            ans = product
            num1,num2 = mylist[i],mylist[j]

print(num1, "and", num2, "give max product:", ans)
        



