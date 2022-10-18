from collections import deque
from itertools import combinations

N = int(input())
res = 2147000000
population = list(map(int, input().split()))
board = [[] for _ in range(10)]
def bfs(combi):
    start = combi[0]
    q = deque([start])
    ch = set([start])
    _sum = 0
    while q:
        v = q.popleft()
        _sum += population[v]
        for i in board[v]:
            if i in combi and i not in ch:
                ch.add(i)
                q.append(i)
    return _sum, len(ch)
for i in range(N):
    area = list(map(int, input().split()))
    for j in range(1, len(area)):
        board[i].append(area[j] - 1)

for i in range(1, N // 2 + 1):
    combis = list(combinations(range(N), i))
    for combi in combis:
        sum1, v1 = bfs(combi)
        sum2, v2 = bfs([i for i in range(N) if i not in combi])
        if v1 + v2 == N:
            res = min(res, abs(sum1 - sum2))
print(res if res != 2147000000 else -1)