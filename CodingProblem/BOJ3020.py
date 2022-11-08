N, H = map(int, input().split())

d = [0] * (H + 1)
u = [0] * (H + 1)
for i in range(N):
    if i % 2 == 0:
        d[int(input())] += 1
    else:
        u[int(input())] += 1

for i in range(H - 1, 0, -1):
    d[i] += d[i + 1]
    u[i] += u[i + 1]
# print(d, u)

min_val = N
res = 0
for i in range(1, H + 1):
    if (d[i] + u[H - i + 1]) < min_val:
        min_val = d[i] + u[H - i + 1]
        res = 1
    elif (d[i] + u[H - i + 1]) == min_val:
        res += 1

print(min_val, res)