"""
A
A B
A B C
A B C D
A B C D E
"""
# for i in range(1,6):
#     x = 65
#     for j in range(1,i+1):
#         print(chr(x),end=" ")
#         x = x+1
    
#     print()

"""
        A
      A B C
    A B C D E
  A B C D E F G
A B C D E F G H I
"""
for i in range(1,6):
    x = 65
    for j in range(1,6-i):
        print(" ",end=" ")
    for k in range(1,i+1):
        print(chr(x),end=" ")
        x = x+1
    for l in range(1,i):
        print(chr(x),end=" ")
        x = x+1

    print()