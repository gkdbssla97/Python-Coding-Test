import copy
from itertools import combinations_with_replacement

n = 10
info = [1,1,1,1,1,0,0,0,0,0,0]

def solution(n, info):
    max_val = 0
    res = [-1]
    for i in list(combinations_with_replacement(range(11), n)):
        ryan_info = [0] * 11
        print(i)
        for x in i:  # (1,1,1,1,1)
            ryan_info[10 - x] += 1
        total = 0

        for j in range(11):
            # print(ryan_info[j], info[j])
            if ryan_info[j] - info[j] > 0:
                total += 10 - j
            elif ryan_info[j] - info[j] < 0:
                total -= 10 - j
            elif ryan_info[j] - info[j] == 0 and \
                    ryan_info[j] != 0 and info[j] != 0:
                total -= 10 - j

        if max_val < total and 0 < total:
            max_val = total
            res = copy.deepcopy(ryan_info)

    return res
# 어피치 10 9 8 3
# 라이언 10 9 7 3
solution(n, info)