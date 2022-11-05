from itertools import combinations
N, K = map(int, input().split())

alpha = {'a', 'n', 't', 'i', 'c'} #필수 배움

#print(bin(learn))
#str = list(input()[4:-4] for _ in range(N))

words = [0] * N
for i in range(N):
    str = input()
    filter_str = str[4:-4]
    for x in filter_str:
        #print(x)
        words[i] |= 1 << (ord(x) - 97)

res = 0

if K < 5:
    print(0)
    exit(0)
else:
    candidate = {chr(i) for i in range(ord('a'), ord('z') + 1)}.difference(alpha)
    #print(candidate)
    for i in combinations(candidate, K - 5):
        # 펭귄이 반드시 알아야 하는 단어
        learn = 0
        learn |= 1 << (ord('a') - 97)
        learn |= 1 << (ord('n') - 97)
        learn |= 1 << (ord('t') - 97)
        learn |= 1 << (ord('i') - 97)
        learn |= 1 << (ord('c') - 97)
        cnt = 0
        #print(i)
        for j in i:
            learn |= 1 << (ord(j) - 97)
        for x in words:
            # print(bin(x), bin(learn))
            # print('----')
            if x & learn == x:
                # print(f'x:{bin(x)}')
                cnt += 1
        res = max(res, cnt)
print(res)