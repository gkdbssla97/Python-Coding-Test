import copy
from collections import deque
places = [list(map(str, input().split())) for _ in range(5)]
'''
POOOP OXXOX OPXPX OOXOX POXXP
POOPX OXPXP PXXXO OXXXO OOOPP
PXOPX OXOXP OXPOX OXXOP PXPOX
OOOXX XOOOX OOOXX OXOOX OOOOO
PXPXP XPXPX PXPXP XPXPX PXPXP
'''
dx = [-1, 0, 1, 0] #북동남서
dy = [0, 1, 0, -1]

def bfs(q):
    p = deque(q)
    while p:
        x, y = p.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5 and ch[nx][ny] == 0\
                    and tmp[nx][ny] == 'O':
                print('!!')
                ch[nx][ny] = 1
                distance[nx][ny] = distance[x][y] + 1
                p.append((nx, ny))
            elif 0 <= nx < 5 and 0 <= ny < 5 and ch[nx][ny] == 0\
                    and tmp[nx][ny] == 'P':
                if distance[x][y] + 1 <= 2:
                    return 0
    return 1

res = []
for num in range(5):
    ch = [[0] * 5 for i in range(5)]
    distance = [[0] * 5 for i in range(5)]
    tmp = copy.deepcopy(places[num])
    q = deque()
    for i in range(5):
        for j in range(5):
            if tmp[i][j] == 'P':
                ch[i][j] = 1
                q.append((i, j))
    res.append(bfs(q))
    for i in range(5):
        print(distance[i])
    print('-----------')
print(res)