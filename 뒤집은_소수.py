def reverse(x):
    tmp = ""
    for i in reversed(str(x)):
        tmp += i
    return int(tmp)

def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x//2 + 1):
        if x % i == 0:
            return False
    return True

N = int(input())
num = list(map(int, input().split()))

for x in num:
    tmp = reverse(x)
    #print(tmp)
    if isPrime(tmp):
        print(tmp, end = ' ')
