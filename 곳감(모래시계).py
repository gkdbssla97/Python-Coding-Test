from collections import deque
N = int(input())

# for i in range(N):
#     gam.append(list(map(int, input().split())))
gam = [list(map(int, input().split())) for _ in range(N)]
# 위와 같이 한 줄로 나타낼 수 있음

M = int(input())
for i in range(M):
    cmd = list(map(int, input().split()))
    # cmd-> 행, 왼/오, x만큼 이동
    sub_gam = deque(gam[cmd[0] - 1])
    if cmd[1] == 0: #LEFT
        for j in range(cmd[2]):
            sub_gam.append(sub_gam.popleft())
        gam[cmd[0] - 1] = list(sub_gam)
    elif cmd[1] == 1: #RIGHT
        for j in range(cmd[2]):
            sub_gam.appendleft(sub_gam.pop())
        gam[cmd[0] - 1] = list(sub_gam)
total_gam = 0
for i in range(N//2):
    total_gam += sum(gam[i][0 + i:N - i])
    total_gam += sum(gam[N - 1 - i][0 + i:N - i])
total_gam += gam[N//2][N//2]
print(total_gam)
'''
5
10 13 10 12 15
12 39 30 23 11
11 25 50 53 15
19 27 29 37 27
19 13 30 13 19
3
2 0 3
5 1 2
3 1 4
'''
