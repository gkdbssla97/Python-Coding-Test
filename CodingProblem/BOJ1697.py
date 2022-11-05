import sys
from collections import deque
N, K = map(int, input().split())

dx = [-1, 1, 2] #이동
ch = [0] * 200000
sys.setrecursionlimit(10**5)

def bfs(v):
    global cnt, res
    q = deque()
    q.append(v)
    while q:
        v = q.popleft()
        if v == K:
            if cnt == 0:
                res = ch[v]
                cnt += 1
            else:
                if ch[v] == res:
                    cnt += 1

        for i in range(3):
            if i == 0 or i == 1:
                nx = v + dx[i]
                if nx < 0 or nx >= 100001:
                    continue
                if (ch[nx] == 0 or ch[nx] == ch[v] + 1) and 0 <= nx <= 200001:
                    ch[nx] = ch[v] + 1
                    q.append(nx)
            else:
                nx = v * dx[i]
                if nx < 0 or nx >= 100001:
                    continue
                if (ch[nx] == 0 or ch[nx] == ch[v] + 1) and 0 <= nx <= 200001:
                    ch[nx] = ch[v] + 1
                    q.append(nx)

cnt = 0
ch[N] = 0
bfs(N)
print(res)
print(cnt)