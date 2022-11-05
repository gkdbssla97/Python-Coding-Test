from collections import deque

N, M = map(int, input().split())

com = [[0] for idx in range(N + 1)]
def bfs(start):
    q = deque()
    q.append(start)
    check[start] = 1
    while q:
        start = q.popleft()
        for i in com[start]:
            if check[i] == 0:
                #print(f'i:{i} ok')
                check[i] = 1
                q.append(i)

for _ in range(M):
    a, b = (map(int, input().split()))
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
        print(idx, end=' ')
    idx += 1


