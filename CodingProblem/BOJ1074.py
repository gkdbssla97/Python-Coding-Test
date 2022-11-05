N, r, c = map(int, input().split())

board = [[0] * (2**N) for i in range(2**N)]

#1번
# val = 0
# for i in range(k//2):
#     for j in range(k//2):
#         board[i][j] = val
#         val += 1
# #2번
# for i in range(k//2):
#     for j in range(k//2, k):
#         board[i][j] = val
#         val += 1
# #3번
# for i in range(k//2, k):
#     for j in range(k//2):
#         board[i][j] = val
#         val += 1
# #4번
# for i in range(k//2, k):
#     for j in range(k//2, k):
#         board[i][j] = val
#         val += 1
#
# N = 2
def sol(N):
    global r, c
    global ans
    while N != 0:
        N -= 1

        # 1사분면
        if r < 2**N and c < 2**N:
            ans += (2 ** N) * (2 ** N) * 0
        # 2사분면
        elif r < 2**N and c >= 2**N:
            ans += (2 ** N) * (2 ** N) * 1
            c -= (2**N)
        # 3사분면
        elif r >= 2 ** N and c < 2 ** N:
            ans += (2 ** N) * (2 ** N) * 2
            r -= (2**N)
        # 4사분면
        elif r >= 2 ** N and c >= 2 ** N:
            ans += (2 ** N) * (2 ** N) * 3
            r -= (2 ** N)
            c -= (2 ** N)



ans = 0
sol(N)
print(ans)