N = list(map(int, input()))

def dfs(v, p):
    global cnt
    if v == n:
        for i in range(p):
            print(chr(res[i] + 64), end = ' ')
        print()
        cnt += 1
    else:
        for i in range(1, 27):
             if N[v] == i:
                res[p] = i
                dfs(v + 1, p + 1)
             elif i >= 10 and N[v] == i // 10 and N[v + 1] == i % 10:
                 res[p] = i
                 dfs(v + 2, p + 1)
cnt = 0
n = len(N)
N.insert(n, -1)
print(N)
res = [0] * (n + 1)
dfs(0, 0)
print(cnt)