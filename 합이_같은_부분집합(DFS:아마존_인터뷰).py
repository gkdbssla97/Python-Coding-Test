N = int(input())

def dfs(Level, sum):
    global switch
    if switch: return
    if Level == N:
        if sum == total - sum:
            print("YES")
            switch = 1

    else:
        dfs(Level + 1, sum + num[Level])
        dfs(Level + 1, sum)

num = list(map(int, input().split()))
max_val = max(num)
total = sum(num)
switch = 0

for idx in num:
    ch = [0 for _ in range(max_val + 1)]
    dfs(0, 0)

    if switch == 0:
        print("NO")
