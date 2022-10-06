N, r, c = map(int, input().split())

def sol(N, r, c):
    global ans
    if N == 0:
        return 0
    ans += 2*(r % 2) + (c % 2) + 4 * sol(N - 1, r // 2, c // 2)
ans = 0
sol(N, r, c)
print(ans)
# (3,1) -> (1,0) #2 * 4