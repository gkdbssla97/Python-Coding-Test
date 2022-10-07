def fib(stack[num][n]):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return stack[num][n]
    else:
        return fib(stack[num][n] - 1) + fib(stack[num][n] - 2)

tmp = list(map(int, input().split()))
queries = []
idx = 0
while idx < len(tmp) - 1:
    a, b = tmp[idx], tmp[idx + 1]
    queries.append([a, b])
    idx += 2

stack = [[] * 1000 for _ in range(10000)]

for idx in range(len(queries)):
    stack[queries[idx][0]].append(queries[idx][1])

num = 0
res_sum = 0
print(stack)
while num < 1000:
    res = 0
    if stack[num]:
        leng = len(stack[num])
        print(f' len:{leng}')
        if leng > 1:
            tmp1 = 0
            tmp1_1 = 0
            size = 1
            tmp2 = 1
            for idx in range(0, leng - 1):
                if idx == leng:
                    break
                tmp1 = stack[num][idx]
                tmp1_1 += stack[num][idx]
                #print(f'tmp1:{tmp1}')
                tmp2 = tmp1_1 + stack[num][idx + 1]
                if size < tmp2:
                    while size < tmp2:
                        size = size * 2
                    print(f'size:{size}')
                res = fib(stack[num][idx])
                print(f'res:{res}')
                print(f'i:{idx}')
        else:
            continue
    num += 1
    res_sum += res
print(res_sum)

# 2 10 7 1 2 5 2 9 7 32
# 1 1 1 2 1 4 1 8
#[[2, 10], [7, 1], [2, 5], [2, 9], [7, 32]]