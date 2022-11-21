#4 2 5 5 4 5 6 3 7 6
from itertools import combinations

make = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
k = int(input())

def dfs(v):
    global total
    if v == k + 1:
        tmp = []
        res = []
        sum = 0
        sum1 = 1
        for i in range(1, k + 1):
            if tree[i] == 1:
                sum += i
                tmp.append(i)
        print(tmp)
        print(sum)
        if sum == k:
            res = tmp
            print(res)
            for i in res:
                sum1 *= make.count(i)
            if len(res) > 1:
                sum1 *= 2
            print(f'sum1: {sum1}')
            total += sum1

        print()
    else:
        tree[v] = 1
        dfs(v + 1)
        tree[v] = 0
        dfs(v + 1)

tree = [0] * (k + 1)
total = 0
dfs(1)
print(total)