N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

def check_road(route):
    bridge = [0] * N
    for i in range(N - 1):
        if route[i] != route[i + 1]:
            if abs(route[i] - route[i + 1]) > 1:
                return False
            else:
                if route[i] - route[i + 1] == 1:
                    check = route[i + 1]
                    if i + 1 + L > N: return False
                    for j in range(i + 1, i + 1 + L):
                        if bridge[j] or route[j] != check:
                            return False
                        bridge[j] = 1
                elif route[i] - route[i + 1] == -1:
                    if i - L + 1 < 0:
                        return False
                    check = route[i]
                    for j in reversed(range(i - L + 1, i + 1)):
                        if bridge[j] or route[j] != check:
                            return False
                        bridge[j] = 1
    return True

garo = []
sero = []

for i in range(N):
    tmp = []
    for j in range(N):
        tmp.append(board[j][i])
    sero.append(tmp)
#print(sero)

cnt = 0
for i in range(N):
    if check_road(board[i]):
        cnt += 1
        #print(f'g:{cnt}')
    if check_road(sero[i]):
        cnt += 1
        #print(f's:{cnt}')
print(cnt)