N, M, H = map(int, input().split())
if M == 0:
    print(0)
    exit(0)

ladder = [[0] * N for _ in range(H)]
#print(ladder)

for idx in range(M):
    x, y = list(map(int, input().split()))
    ladder[x - 1][y - 1] = 1
# for idx in range(H):
#     print(ladder[idx])

def check():
    for i in range(N): #세로
        k = i
        for j in range(H): #가로
            if ladder[j][k] == 1: #가로 오른쪽
                k += 1
            elif k > 0 and ladder[j][k - 1] == 1:
                k -= 1
        if k != i:
            return False
    return True

def dfs(x, y, cnt):
    global ans
    if check():
        ans = min(ans, cnt)
        #return
    elif cnt == 3 or ans <= cnt:
        return
    else:
        for i in range(x, H): #가로선
            if i == x:
                k = y
            else:
                k = 0
            for j in range(k, N - 1): #세로선
                if ladder[i][j] == 0 and ladder[i][j + 1] == 0:
                    if j > 0 and ladder[i][j - 1] != 0:
                        continue
                    ladder[i][j] = 1
                    dfs(i, j + 2, cnt + 1)
                    ladder[i][j] = 0

#print('start')
#N 세로, M 가로, 추가 H
ans = 4
dfs(0, 0, 0)
print(ans if ans < 4 else -1)