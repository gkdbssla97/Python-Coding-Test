N, M = map(int, input().split())
tree = list(map(int, input().split()))

s = 0
e = max(tree)

res_mid = 0
while s <= e:
    sum = 0
    mid = (s + e) // 2
    #print(f'mid:{mid}')
    for i in tree:
        if i > mid:
            sum += i - mid
    #print(f'sum:{sum}')
    if M <= sum:
        s = mid + 1
        res_mid = mid
    elif M > sum:
        e = mid - 1
    # if s > e:
    #     break

print(res_mid)
