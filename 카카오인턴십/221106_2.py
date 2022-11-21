import math
from itertools import combinations

def solution(cost, x):
    # Write your code here
    max_val = (0,)
    cost_arr = [i for i in range(0, len(cost))]

    if sum(cost) < x:
        res = 0
        for x in cost_arr:
            res += 2 ** x
        return res

    for length in reversed(range(1, len(cost))):
        total = 0
        arr = []
        for i in list(combinations(cost_arr, length)):
            print(i)
            if cost[i[::-1][0]] > x:
                continue
            total = 0
            for idx in i:
                total += cost[idx]
            if total > x: continue
            print(f'total{total}')
            if total > x or max_val > i[::-1]:
                continue
            if total <= x and max_val <= i[::-1]:
                print(i[::-1])
                print(total)
                max_val = i[::-1]
    res = 0
    print(f'!{max_val}')

    for x in max_val:
        res += 2**x
        print(x**2)
    return res

n = 3
cost = [19,78,27,18,20]
x = 25
print(solution(cost, x))
