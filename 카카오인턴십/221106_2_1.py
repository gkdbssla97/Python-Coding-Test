import sys
sys.setrecursionlimit(10**6)

def recursion(size):
    global total
    global x
    global ans
    global res

    for i in reversed(range(0, size + 1)):
        total = cost[i]
        ans += total

        if ans <= x:
            res.append(i)
            recursion(size - 1)
            break
        else:
            ans -= total
            if size == 0:
                return res


def solution(cost, x):
    size = len(cost) - 1 # 5
    recursion(size)

# cost = [10, 20, 14, 40, 50]
# x = 70
# cost = [3,4,1]
# x= 8
cost = [19,78,27,18,20]
x = 25
total = 0
ans = 0
res = []
solution(cost, x)
final_answer = 0

for i in range(len(res)):
    final_answer += 2**res[i]
print(final_answer)
