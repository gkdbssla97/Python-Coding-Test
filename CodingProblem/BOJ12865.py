N, K = map(int, input().split())
K += 1
bag = [tuple(map(int, input().split())) for _ in range(N)]
bag.sort(reverse=True)

dp = {0: 0}
for w, v in bag:
    tmp = {}
    for dp_v, dp_w in dp.items():
        print(f'dp_v:{dp_v} dp_w:{dp_w}')
        if dp.get(nv := dp_v + v, K) > (nw := dp_w + w):
            print(dp.get(nv := dp_v + v, K), (nw := dp_w + w))
            tmp[nv] = nw
    dp.update(tmp)
    print(dp)
print(max(dp.keys()))


'''
4 7
6 13
4 8
3 6
5 12
'''

