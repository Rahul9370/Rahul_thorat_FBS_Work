"""
1
2 3
4 5 6
7 8 9 10
"""
# num = 1
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(num,end=" ")
#         num += 1
    
#     print()

'''
   1
  1 1
 1 2 1
1 3 3 1   
'''
# for i in range(1,5):
#     for j in range(1,5-i):
#         print(" ",end="")
#     for k in range(1,i+1):
#         if(i==3 and k==2):
#             print(2,end=" ")
#         elif(i==4 and (k==2 or k==3)):
#             print(3,end=" ")
#         else:
#             print(1,end=" ")

#     print()

'''
        1
      1 2 3
    1 2 3 4 5
  1 2 3 4 5 6 7
1 2 3 4 5 6 7 8 9 
'''
for i in range(1, 6):
    for j in range(1, 6 - i):
        print(" ", end=" ")
    for k in range(1, i + 1):
        print(k, end=" ")
    n = i + 1
    for l in range(1, i):
        print(n, end=" ")
        n += 1

    print()
