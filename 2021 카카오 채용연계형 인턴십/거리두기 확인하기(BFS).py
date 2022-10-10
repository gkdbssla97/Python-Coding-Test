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

def bfs(s):
    p = deque(s)
    while p:
        x, y = p.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5 and ch[nx][ny] == -1\
                    and tmp[nx][ny] == 'O':
                ch[nx][ny] = ch[x][y] + 1
                p.append((nx, ny))
            elif 0 <= nx < 5 and 0 <= ny < 5 and ch[nx][ny] == -1\
                    and tmp[nx][ny] == 'P':
                if ch[x][y] + 1 <= 2:
                    return 0
    return 1

distance = []
res = []
for num in range(5):
    ch = [[-1] * 5 for i in range(5)]
    tmp = copy.deepcopy(places[num])
    start = []
    for i in range(5):
        for j in range(5):
            if tmp[i][j] == 'P':
                start.append([i, j])
    for s in start:
        ch[s[0]][s[1]] = 0
        distance.append(bfs([s]))
        # for i in range(5):
        #     print(ch[i])
    # print(distance)
    # print('----')
    # for i in range(5):
    #     print(ch[i])
    # print('-----')
    if distance.count(0) > 0:
        res.append(0)
    else: res.append(1)
    distance = []
    # for i in range(5):
    #     print(ch[i])
    # print('-----------')
print(res)