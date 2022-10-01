N = int(input())

dx = [0] * (N + 1)
dx[1] = 1
dx[2] = 2
def dfs(len):
    if dx[len] > 0:
        return dx[len]
    if len == 1 or len == 2:
        return len
    else:
        dx[len] = dfs(len - 1) + dfs(len - 2)
        return dx[len]

print(dfs(N))