'''
     *
    * *
   *   *
  *     *
 *       *
 *       *
  *     *
   *   *
    * *
     * 
'''
# for i in range(5):
#     print(" " * (4 - i), end="")  
#     print("*", end="")           

#     if i != 0:
#         print(" " * (2 * i - 1), end="")  
#         print("*", end="")               
#     print()

# for i in range(4, -1, -1):
#     print(" " * (4 - i), end="")  
#     print("*", end="")          

#     if i != 0:
#         print(" " * (2 * i - 1), end="")  
#         print("*", end="")               
#     print()
#or
# for i in range(1,6):
#     for j in range(1,6-i):
#         print(" ",end="")
#     for k in range(1,7-i):
#         if(k==1):
#             print("*",end="")
#     for l in range(1,i):
#         print(" ",end="") 
#     for m in range(1,i):
#         if(m==1 and i==2 or m==2 and i==3 or m==3 and i==4 or m==4 and i==5):
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()

# for i in range(1,6):
#     for j in range(1,i):
#         print(" ",end="")
#     for n in range(1,i+1):
#         if(n==1):
#             print("*",end="")
#     for l in range(1,6-i):
#         print(" ",end=" ")
#     for m in range(1,2):
#         if(i==5 and m==1):
#             print("",end="") 
#         else:
#             print("*",end="")
#     print()

'''
*
* *
* * * 
* * * *
* * * * *
* * * *
* * *
* *
*
'''
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for k in range(1,5):
    for l in range(1,6-k):
        print("*",end=" ")
    print()