N = int(input())

coin = []
for _ in range(N):
    coin.append(int(input()))

def dfs(v, mem):
    global res
    if v == N:
        num = max(mem) - min(mem)
        tmp = set()
        for x in mem:
            tmp.add(x)
        if len(tmp) == 3:
            if res > num:
                res = num

    else:
        for i in range(3):
            mem[i] += coin[v]
            dfs(v + 1, mem)
            mem[i] -= coin[v]

res = 2147000000
mem = [0] * 3
dfs(0, mem)
print(res)
'''
7
8
9
11
12
23
15
17
'''