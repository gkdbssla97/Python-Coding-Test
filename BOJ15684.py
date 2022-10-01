N, M, H = map(int, input().split())

ladder = [[0] * M for _ in range(N)]
#print(ladder)

road = []
for i in range(M):
    x, y = list(map(int, input().split()))
    road.append([x - 1, y - 1])
for x, y in road:
    ladder[x][y] = 1
    ladder[x][y + 1] = 1
for i in range(M):
    print(ladder[i])