import math

n = int(input())

def cal_sqrt(n):
# 1개 일때
    if math.sqrt(n) == int(math.sqrt(n)):
        return 1

    # 2개 일때
    for i in range(1, int(math.sqrt(n)) + 1):
        if math.sqrt(n - i**2) == int(math.sqrt(n - i**2)):
            return 2

    # 3개 일때
    for i in range(1, int(math.sqrt(n)) + 1):
        for j in range(1, int(math.sqrt(n - i**2)) + 1):
            if int(math.sqrt(n - i**2 - j**2)) == (math.sqrt(n - i**2 - j**2)):
                return 3

    return 4
print(cal_sqrt(n))

