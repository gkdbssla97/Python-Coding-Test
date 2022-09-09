N, K = map(int, input().split())

num = list(map(int, input().split()))
M = int(input())

def dfs(v, s):
    global cnt
    if v == K:
        sum = 0
        for i in pick:
            print(i, end= ' ')
            sum += i
        if sum % M == 0:
            cnt += 1
        print()
    else:
        for i in range(s, N):
            pick[v] = num[i]
            dfs(v + 1, i + 1)

cnt = 0
pick = [0 for _ in range(K)]
dfs(0, 0)
print(cnt)