from collections import deque

N, M, B = map(int, input().split())
mm = [list(map(int, input().split())) for _ in range(N)]
height = 0
res = 21470000

for idx in range(257):
    max, min = 0, 0
    for j in range(N):
        for k in range(M):
            if mm[j][k] < idx:
                min += (idx - mm[j][k])
            else:
                max += (mm[j][k] - idx)
    #print(f'i: {i} max:{max}, min:{min}')
    inventory = max + B
    if inventory < min:
        continue
    time = 2 * max + min

    if time <= res:
        res = time
        height = idx

print(res, height)