# WAP to print Z shape using star pattern
"""
*****
   *
  *
 *
*****
"""
def Pattern(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == 1 or i == n:        
                print("*", end="")
            elif j == n - i + 1:        
                print("*", end="")
            else:
                print(" ", end="")
        print()


Pattern(10)
