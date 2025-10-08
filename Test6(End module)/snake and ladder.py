# 2. snake and ladder board. use ">:" for snake's head (use random 7 numbers for snake's head using random module).
# Hint:
# 21 >: 23 24 25 26 27 28 29 30
# 20 19 18 17 >: 15 14 13 12 11
import random

def create_board():
    snake_heads = random.sample(range(11, 31), 7)   
    print("Snake heads at positions:", snake_heads)
    print("\nSnake and Ladder Board:\n")

    num = 21
    for i in range(3):   
        row = []
        for j in range(10):
            if num in snake_heads:
                row.append(">:")
            else:
                row.append(f"{num:02d}")
            num += 1
        
        if i % 2 == 1:
            row.reverse()
        print(" ".join(row))
        num -= 20  

create_board()
