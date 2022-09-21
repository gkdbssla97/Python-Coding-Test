N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
ch = []
hs = []
pick = [0] * M

def dfs(v, s):
    global res
    if v == M: #조합 한세트 완성된 if문
        sum = 0
        for x1, y1 in hs:
            min_val = 21470000
            for val in pick: # [0 1 2]
                x2 = ch[val][0]
                y2 = ch[val][1]
                dis = abs(x1 - x2) + abs(y1 - y2)
                if min_val > dis:
                    min_val = dis
            sum += min_val
        if res > sum:
            res = sum
    else:
        for i in range(s, len_ch):
            pick[v] = i
            dfs(v + 1, i + 1)

for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            hs.append((i, j))
        elif board[i][j] == 2:
            ch.append((i, j))

res = 2147000000
len_ch = len(ch)
dfs(0, 0) # v, s
print(res)