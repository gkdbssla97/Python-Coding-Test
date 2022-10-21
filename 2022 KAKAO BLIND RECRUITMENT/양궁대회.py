import copy
from itertools import combinations_with_replacement

n = 5
info = [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]

# 동률 또는 점수취득
max_val = 0
res = []
for i in list(combinations_with_replacement(range(11), n)):
    ryan_info = [0] * 11
    for x in i: #(1,1,1,1,1)
        ryan_info[10 - x] += 1
    total = 0

    for j in range(11):
        # print(ryan_info[j], info[j])
        if ryan_info[j] - info[j] > 0:
            total += 10 - j
        elif ryan_info[j] - info[j] < 0:
            total -= 10 - j
        elif ryan_info[j] - info[j] == 0 and\
                ryan_info[j] > 0 and info[j] > 0:
            total -= 10 - j

    if max_val < total:
        max_val = total
        res = copy.deepcopy(ryan_info)
    elif max_val == total:
        if res > ryan_info:
            res = ryan_info
print(res if max_val != 0 else [-1])
#print(max_val)




