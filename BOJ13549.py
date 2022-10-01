import sys
from collections import deque

input = sys.stdin.readline
N, K = map(int, input().split())
ch = [0 for _ in range(100001)]

def bfs(x):
    q = deque()
    q.append(x)
    while q:
        x = q.popleft()
        if x == K:
            print(ch[K])
            break
        for i in (x + 1, x - 1, x * 2):
            if 0 <= i < 100001 and ch[i] == 0:
                if i == x * 2:
                    ch[i] = ch[x]
                    q.appendleft(i)

                else:
                    ch[i] = ch[x] + 1
                    q.append(i)

#ch[N] = 0
bfs(N)
#print(ch[K])