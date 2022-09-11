from collections import deque
S, E = map(int, input().split())

d = [1, -1, 5]
MAX = 10000
ch = [0] * (MAX + 1)
dis = [0] * (MAX + 1)

def bfs(S, E):
    global cnt
    q = deque()
    q.append(S)

    while q:
        x = q.popleft()
        if x == E:
            break
        for i in range(3):
            nx = x + d[i]
            if 0 <= nx <= MAX:
                if ch[nx] == 0:
                    q.append(nx)
                    ch[nx] = 1
                    dis[nx] = dis[x] + 1
cnt = 0
ch[S] = 1
dis[S] = 0
bfs(S, E)
print(dis[E])