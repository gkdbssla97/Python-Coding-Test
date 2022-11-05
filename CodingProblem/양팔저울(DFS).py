K = int(input())
chu = list(map(int, input().split()))

def dfs(v, sum):
    global res
    if v == K:
        if 0 < sum <= s:
            res.add(sum)
    else:
        dfs(v + 1, sum + chu[v]) #왼쪽(+)
        dfs(v + 1, sum - chu[v]) #오른쪽(-)
        dfs(v + 1, sum) #올려놓지않음 ()


s = sum(chu)
res = set()
dfs(0, 0)
print(s - len(res))