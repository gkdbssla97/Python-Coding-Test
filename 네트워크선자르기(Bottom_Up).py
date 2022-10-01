N = int(input())

dx = [0] * (N + 1)
dx[1] = 1
dx[2] = 2
for i in range(3, N + 1):
    dx[i] = dx[i - 1] + dx[i - 2]
print(dx[N])