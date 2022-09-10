N = int(input())

pick = []
for _ in range(N):
    x, y = map(int, input().split())
    pick.append((x, y))
pick.sort(key = lambda x:(x[1], x[0]))

for x, y in pick:
    print(x, y)