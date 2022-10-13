from itertools import combinations
from collections import deque

N, M, k = map(int, input().split())
friend_fee = [0] + list(map(int, input().split()))
parent = [x for x in range(N + 1)]
res = 2147000000
print(friend_fee)
print(parent)
def find(target):
    if target == parent[target]:
        return target
    parent[target] = find(parent[target])
    return parent[target]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        if friend_fee[a] <= friend_fee[b]:
            parent[b] = a
        else:
            parent[a] = b

for i in range(M):
    v, w = map(int, input().split())
    union(v, w)

total = 0
tmp = set()
for i in range(1, N + 1):
    a = find(i)
    if a in tmp:
        continue
    else:
        tmp.add(a)
        total += friend_fee[a]
# print(total)
# print(tmp)
print(total if total <= k else "Oh no")