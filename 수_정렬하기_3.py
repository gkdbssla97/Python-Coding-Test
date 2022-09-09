import sys
N = sys.stdin.readline(int(input()))

num = []
for _ in range(N):
    num.append(int(input()))
num.sort()
for i in num:
    print(i)
