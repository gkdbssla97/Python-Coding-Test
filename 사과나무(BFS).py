from collections import deque
S, E = map(int, input().split())

dx = [-1, 1, 5]

def bfs(S, E):
    q = deque()
    q.append(S)
    while q:
        x = q.popleft()
        if x == E:
            break
        for i in range(3):
            nx = x + dx[i]
            if 10000 >= nx >= 0 and ch[nx] == 0:
                ch[nx] = 1
                q.append(nx)
                dis[nx] = dis[x] + 1

ch = [0] * 10001
ch[S] = 1
dis = [0] * 10001
dis[S] = 0
bfs(S, E)
print(dis[E])