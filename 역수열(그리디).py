N = int(input())
arr = list(map(int, input().split()))
res = [0 for _ in range(N)]
pick = []
for idx in range(N):
    for j in range(N):
        if res[j] == 0 and arr[idx] == 0:
            res[j] = idx + 1
            break
        elif res[j] == 0:
            arr[idx] -= 1

for idx in range(N):
    print(res[idx], end =' ')
'''
8
5 3 4 0 2 1 1 0
'''