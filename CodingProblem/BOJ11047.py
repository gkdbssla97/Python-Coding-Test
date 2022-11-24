N, K = map(int, input().split())

money = []
for _ in range(N):
    money.append(int(input()))

cnt = 0
for i in reversed(range(0, N)):
    if K >= money[i]:
        # print(K, money[i])
        cnt += K // money[i]
        K = K - (K // money[i]) * money[i]
    if K == 0:
        print(cnt)
        break
