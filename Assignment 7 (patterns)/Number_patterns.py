'''
1
1 2
1   3
1     4
1 2 3 4 5
'''
# for i in range(1, 6):
#     for j in range(1, i + 1):
#         if j == 1 or j == i or i == 5:
#             print(j, end=" ")
#         else:
#             print(" ", end=" ")
#     print()

'''
        1
      2 3 2
    3 4 5 4 3
  4 5 6 7 6 5 4
5 6 7 8 9 8 7 6 5        
'''
# for i in range(1, 6):
#     for j in range(1,6-i):
#         print(" ", end=" ")

#     for k in range(i):
#         print(i + k, end=" ")

#     for l in range(i - 2, -1, -1):
#         print(i + l, end=" ")

#     print()


'''
    1
   1 2
  1   3
 1     4
1 2 3 4 5
'''
# for i in range(1, 6):
#     for j in range(5 - i):
#         print(" ", end="")

#     for k in range(1, i + 1):
#         if k == 1 or k == i or i == 5:
#             print(k, end=" ")
#         else:
#             print(" ", end=" ")

#     print()

"""
1 2 3 4 5
2     5
3   5
4 5
5
"""
# for i in range(1, 6):
#     for j in range(i, 6):
#         if i == 1:
#             print(j, end=" ")
#         elif j == i or j == 5:
#             print(j, end=" ")
#         else:
#             print("  ", end="")  # Two spaces for alignment
#     print()

'''
        1 
      1 2 1 
    1 2 3 2 1 
  1 2 3 4 3 2 1  
1 2 3 4 5 4 3 2 1 
'''
# for i in range(1,6):
#     for j in range(5-i):
#         print(" ",end=" ")
#     for k in range(1,i+1):
#         print(k,end=" ")
#     for l in range(1,i):
#         k=k-1
#         print(k,end=" ")
#     print()

'''
1               1
1 2           2 1
1 2 3       3 2 1
1 2 3 4   4 3 2 1
1 2 3 4 5 4 3 2 1
'''
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    for k in range(2*(5-i)-1):
        print(" ",end=" ")
    for l in range(i,0,-1):
        if(i!=5 or l!=5):
            print(l,end=" ")
    print()

