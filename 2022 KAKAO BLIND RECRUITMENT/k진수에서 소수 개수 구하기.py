import math

n = 110011
k = 10


def solution(n, k):

    arr = ""
    while n != 0:
        arr = str(n % k) + arr
        n //= k

    res = arr.split('0')
    #print(res)
    cnt = 0

    for i in res:
        if len(i) == 0:
            continue
        if int(i) < 2:
            continue

        else:
            sosu = True
            for x in range(2, int(math.sqrt(int(i)) + 1)):
                if int(i) % x == 0:
                    sosu = False
            if sosu:
                cnt += 1
    # print(cnt)

    return cnt

print(solution(n, k))