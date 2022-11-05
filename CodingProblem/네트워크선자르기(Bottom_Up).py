N = int(input())

dx = [0] * (N + 1)
dx[1] = 1
dx[2] = 2
for idx in range(3, N + 1):
    dx[idx] = dx[idx - 1] + dx[idx - 2]
print(dx[N])