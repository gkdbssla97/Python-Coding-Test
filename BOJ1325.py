from collections import deque

N, M = map(int, input().split())

def bfs(v):
    q = deque()
    q.append(v)
    check[v] = 1
    while q:
        v = q.popleft()
        for i in com[v]:
            if check[i] == 0:
                check[i] = 1
                q.append(i)
com = [[0] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    com[b].append(a)

cnt = []
for idx in range(1, N + 1):
    check = [0 for _ in range(N + 1)]
    bfs(idx)
    cnt.append(check.count(1))

max_val = max(cnt)
idx = 1
for idx in cnt:
    if max_val == idx:
       print(idx, end = ' ')
    idx += 1