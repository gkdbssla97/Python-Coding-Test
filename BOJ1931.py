N = int(input())

confer = [list(map(int, input().split())) for _ in range(N)]
confer.sort(key = lambda x: (x[1], x[0]))

cnt = 0
first_start = 0
first_end = 0
for s, e in confer:
    if s >= first_end:
        first_end = e
        cnt += 1
print(cnt)