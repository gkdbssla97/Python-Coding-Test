from itertools import combinations
N = int(input())
mp, mf, ms, mv = map(int, input().split())
food = [list(map(int, input().split())) for _ in range(N)]

sum_mp, sum_mf, sum_ms, sum_mv, sum_price = 0, 0, 0, 0, 0
ans = 2147000000
candidate = []
food_idx = [i for i in range(1, N + 1)]
price = []
for num in range(1, N + 1):
    for i in combinations(food_idx, num):
        for x in i:
            sum_mp += food[x - 1][0]
            sum_mf += food[x - 1][1]
            sum_ms += food[x - 1][2]
            sum_mv += food[x - 1][3]
            sum_price += food[x - 1][4]
        if sum_mp >= mp and sum_mf >= mf and sum_ms >= ms and\
            sum_mv >= mv:
            if ans > sum_price:
                ans = sum_price
                candidate = i
            if ans == sum_price:
                candidate = sorted((candidate, i))[0]
                #print(f'ans: {ans} sum: {sum_price}')

        sum_mp, sum_mf, sum_ms, sum_mv, sum_price = 0, 0, 0, 0, 0
if len(candidate) == 0:
    print(-1)
    exit(0)
print(ans)
print(*candidate)






