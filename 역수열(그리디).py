N = int(input())
arr = list(map(int, input().split()))
res = [0 for _ in range(N)]
pick = []
for i in range(N):
    for j in range(N):
        if res[j] == 0 and arr[i] == 0:
            res[j] = i + 1
            break
        elif res[j] == 0:
            arr[i] -= 1

for i in range(N):
    print(res[i], end = ' ')
'''
8
5 3 4 0 2 1 1 0
'''