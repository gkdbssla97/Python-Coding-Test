N = int(input())

apple_tree = []
for _ in range(N):
    apple_tree.append(list(map(int, input().split())))

get_apple = 0
for i in range(0, N//2):
    get_apple += sum(apple_tree[i][N//2 - i:N//2 + 1 + i])
    #print(f'apple_top:{get_apple}')
    get_apple += sum(apple_tree[N - i - 1][N//2 - i:N//2 + 1 + i])
    #print(f'apple_bottom:{get_apple}')
get_apple += sum(apple_tree[N//2])
'''
res = 0
s=e=n//2
for i in range(N):
    for j in range(s, e+1):
        res += apple_tree[i][j]
    if i < N // 2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1
'''
    # 2: 3
    # 1: 4
print(get_apple)
'''
5
10 13 10 12 15
12 39 30 23 11
11 25 50 53 15
19 27 29 37 27
19 13 30 13 19

'''