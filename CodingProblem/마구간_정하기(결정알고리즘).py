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
#위의 combination은 시간초과
lt = 1
rt = max(location)
location.sort()

while True:
    cnt = 1
    mid = (lt + rt) // 2
    tmp = location[0]
    for idx in location:
        if abs(tmp - idx) >= mid:
            cnt += 1
            tmp = idx
    if cnt < C:
        rt = mid - 1
    elif cnt >= C:
        res = mid
        lt = mid + 1
    if lt > rt:
        break
print(res)
#가장 가까운 두 말의 최대 거리
'''
5 3
1
2
8
4
9
'''