from collections import deque
from itertools import permutations

N = int(input())
SCV = [0, 0, 0]
if N == 1:
    SCV[0] = int(input())
elif N == 2:
    SCV[0], SCV[1] = map(int, input().split())
elif N == 3:
    SCV[0], SCV[1], SCV[2] = map(int, input().split())

attack = [[9, 3, 1], [9, 1, 3], [3, 9, 1], [3, 1, 9],
          [1, 3, 9], [1, 9, 3]]
#permu = list(permutations(attack, 3))
#print(permu)
val = max(SCV) + 1
ch = [[[0] * (val) for i in range(val)] for j in range(val)]

def bfs(SCV):
    q = deque()
    q.append(SCV)
    ch[SCV[0]][SCV[1]][SCV[2]] = 0
    idx = 0
    while q:
        x, y, z = q.popleft()
        #print(f'x,y,z:{x}, {y}, {z}')
        if ch[0][0][0] != 0: break
        for i in attack: #6가지
            idx += 1
            nx = x - i[0]
            ny = y - i[1]
            nz = z - i[2]
            #print(i[0], i[1], i[2])
            # print(f'nx,ny,nz:{nx}, {ny}, {nz}')
            nx = 0 if nx <= 0 else nx
            ny = 0 if ny <= 0 else ny
            nz = 0 if nz <= 0 else nz

            if ch[nx][ny][nz] == 0:
                ch[nx][ny][nz] = ch[x][y][z] + 1

                q.append((nx, ny, nz))


bfs(SCV)
print(ch[0][0][0])


