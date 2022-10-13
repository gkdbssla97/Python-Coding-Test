from itertools import combinations
from collections import deque

N, M, k = map(int, input().split())
friend_fee = list(map(int, input().split()))
friend = [[] for _ in range(N)]
res = 2147000000

def bfs(v):
    # start = v[0]
    q = deque(v)
    mate = set(v)
    while q:
        x = q.popleft()
        for u in friend[x]:
            if u not in mate:
                q.append(u)
                mate.add(u)
    # print(f'mate:{mate}')
    # print(len(mate))
    return len(mate)

for _ in range(M):
    a, b = map(int, input().split())
    friend[a - 1].append(b - 1)
    friend[b - 1].append(a - 1)
# print(friend)

for i in range(1, N // 2 + 1):
    combi = list(combinations(range(N), i))
    for x in combi:
        total = 0
        # print(f'x: {x}')
        if bfs(x) == N:
            for fee in x:
                total += friend_fee[fee]
            #     print(f'fee:{fee}')
            # print(f'total:{total}')
            res = min(res, total)

        total = 0
        tmp = [y for y in range(N) if y not in x]
        # print(f'tmp: {tmp}')
        if bfs(tmp) == N:
            for fee in tmp:
                total += friend_fee[fee]
            #     print(f'tfee:{fee}')
            # print(f'ttotal:{total}')
            res = min(res, total)
        # print(f'res:{res}')
print(res if res <= k else "Oh no")