import math

def changenumber(n, k):
    res = ""
    while n != 0:
        res += str(n % k)
        n //= k
    res = res[::-1]
    print(res)
    return res

def prime(x):
    x = int(x)
    flag = False
    for i in range(2, (int)(math.sqrt(x)) + 1):
        if x % i == 0:
            flag = True
            break

    return flag

def solution(n, k):
    split = changenumber(n, k).split('0')
    print(split)
    cnt = 0
    for x in split:
        if x == '1' or x == '':
            continue
        elif not prime(x):
            cnt += 1

    return cnt

