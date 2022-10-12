import collections
from itertools import combinations
from collections import deque

N = int(input())
population = list(map(int, input().split()))
board = [[] for _ in range(N + 1)]
res = 2147000000

def bfs(combi):
    start = combi[0]
    q = deque([start])
    ch = set([start])
    _sum = 0
    while q:
        v = q.popleft()
        _sum += population[v]
        for u in board[v]:
            if u not in ch and u in combi:
                q.append(u)
                ch.add(u)
    return _sum, len(ch)

for idx in range(N):
    area = list(map(int, input().split()))
    for i in range(1, len(area)):
        board[idx].append(area[i] - 1)
#print(board)

for i in range(1, N // 2 + 1):
    combis = list(combinations(range(N), i))
    for combi in combis:
        sum1, v1 = bfs(combi)
        sum2, v2 = bfs([i for i in range(N) if i not in combi])
        if v1 + v2 == N:
            res = min(res, abs(sum1 - sum2))

print(res if res != 2147000000 else - 1)
