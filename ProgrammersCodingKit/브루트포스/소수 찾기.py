import math
from itertools import combinations_with_replacement
from itertools import permutations
def prime(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x + 1)) + 1):
        if x % i == 0:
            return False
    return True

def solution(numbers):
    visited = [1, 1] + [0] * 10**7
    arr = []
    for x in numbers:
        arr.append(x)

    cnt = 0
    for N in range(1, len(arr) + 1):
        for x in permutations(arr, N):
            # print(x)
            if len(x) == 1:
                if prime(int(x[0])) and visited[int(x[0])] == 0:
                    cnt += 1
                    visited[int(x[0])] = 1

            else:
                tmp = ''.join(x)
                if prime(int(tmp)) and visited[int(tmp)] == 0:
                    cnt += 1
                    # print(int(tmp))
                    visited[int(tmp)] = 1
    return cnt

print(solution("011"))