import sys
N = int(sys.stdin.readline())

#tmp = [0 for _ in range(10001)]
tmp = [0] * 10001
for idx in range(N):
    val = int(sys.stdin.readline())
    tmp[val] += 1
#print(tmp)
for idx in range(10001):
    if tmp[idx] != 0:
        for j in range(tmp[idx]):
            print(idx)
