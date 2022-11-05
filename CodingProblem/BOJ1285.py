N = int(input())
coin = [list(map(str, input())) for _ in range(N)]

res = N * N
for bit in range(1 << N):
    tmp = [coin[i][:] for i in range(N)]
    for i in range(N):
        if bit & (1 << i):
            #print(f'bit: {bin(bit)} com: {1<<i}')
            for j in range(N):
                if tmp[i][j] == 'T':
                    tmp[i][j] = 'H'
                else:
                    tmp[i][j] = 'T'
    tsum = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if tmp[j][i] == 'T':
                cnt += 1
        tsum += min(cnt, N - cnt)
    res = min(res, tsum)
print(res)