import sys
from collections import deque

def bfs():
    q = deque()
    q.append((home_x, home_y))

    while q:
        x, y = q.popleft()
        if abs(x - des_x) + abs(y - des_y) <= 1000:
            return "happy"
        for i in range(cu):
            if not visited[i]:
                new_x, new_y = cu_arr[i]
                if abs(new_x - x) + abs(new_y - y) <= 1000:
                    visited[i] = 1
                    q.append((new_x, new_y))
    return "sad"

t = int(input())

for _ in range(t):
    cu = int(input())
    home_x, home_y = map(int, (input().split()))
    cu_arr = []
    for _ in range(cu):
        cu_arr.append(list(map(int, input().split())))
    # print(cu_arr)
    des_x, des_y = map(int, input().split())
    visited = [0 for i in range(cu + 1)]
    print(bfs())
