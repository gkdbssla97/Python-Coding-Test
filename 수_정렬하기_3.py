import sys
N = int(sys.stdin.readline())

#tmp = [0 for _ in range(10001)]
tmp = [0] * 10001
for i in range(N):
    val = int(sys.stdin.readline())
    tmp[val] += 1
#print(tmp)
for i in range(10001):
    if tmp[i] != 0:
        for j in range(tmp[i]):
            print(i)
