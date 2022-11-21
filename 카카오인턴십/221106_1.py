import math

def solution(x, y, z):
    # Write your code here
    for i in reversed(range(x, x + z + 1)):
        can_move_time = z - (i - x)
        if (i - can_move_time) <= y\
            and (i + can_move_time) >= y:
                return i

    return -1


x, y, z = 8, 5, 3
print(solution(x, y, z))