from collections import deque

subin, sister = map(int, input().split())
ch = [0] * 100001
trace = [0] * 100001
dx = [-1, 1, 2]
def bfs(x):
    q = deque()
    q.append(x)
    while q:
        x = q.popleft()
        if x == sister:
            path = []
            print(ch[x])
            tmp = x
            for _ in range(ch[x] + 1):
                path.append(tmp)
                tmp = trace[tmp]
            print(*path[::-1])
            break
        for i in range(3):
            if i == 2:
                nx = x * dx[i]
            else:
                nx = x + dx[i]
            if 0 <= nx < 100001 and ch[nx] == 0:
                ch[nx] = ch[x] + 1
                q.append(nx)
                trace[nx] = x
bfs(subin)