import math
import sys

input = sys.stdin.readline
N = int(input())

def isPrime(val):
    for i in range(2, int(math.sqrt(val)) + 1):
        if val % i == 0:
            return False
    return True

def dfs(val):
    if len(str(val)) == N:
        print(val)
    else:
        for i in range(10):
            tmp = val * 10 + i
            if isPrime(tmp):
                dfs(tmp)
dfs(2)
dfs(3)
dfs(5)
dfs(7)