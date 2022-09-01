def dfs(v):
    if v == N + 1:
        for i in range(1, N+1):
            if tree[i] == 1:
                print(i, end = ' ')
        print()
    else:
        tree[v] = 1
        dfs(v + 1)
        tree[v] = 0
        dfs(v + 1)


N = int(input())
tree = [0] * (N + 1)
dfs(1)
