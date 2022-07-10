from itertools import combinations
from collections import deque
N, C = map(int, input().split())

location = []
for _ in range(N):
    location.append(int(input()))
#location.sort()
'''
if C == 2:
    print(max(location) - min(location))
else:
    pick = list(combinations(location, 3))
    max_distance = 0
    for i in pick:
        res = []

        for j in range(len(i) - 1):
            res.append(abs(int(i[j]) - int(i[j+1])))
        #res.sort()
        val = min(res)
        if max_distance < val:
            max_distance = val
    print(max_distance)
'''
lt = 1
rt = max(location)
location.sort()

while True:
    cnt = 1
    mid = (lt + rt) // 2
    tmp = location[0]
    for i in location:
        if abs(tmp - i) >= mid:
            cnt += 1
            tmp = i
    if cnt < mid:
        rt = mid - 1
    elif cnt >= mid:
        res = mid
        lt = mid + 1
    if lt > rt:
        break
print(res)
'''
5 3
1
2
8
4
9
'''