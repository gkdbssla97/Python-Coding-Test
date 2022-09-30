def fib(stack[num][n]):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return stack[num][n]
    else:
        return fib(stack[num][n] - 1) + fib(stack[num][n] - 2)

tmp = list(map(int, input().split()))
queries = []
i = 0
while i < len(tmp) - 1:
    a, b = tmp[i], tmp[i + 1]
    queries.append([a, b])
    i += 2

stack = [[] * 1000 for _ in range(10000)]

for i in range(len(queries)):
    stack[queries[i][0]].append(queries[i][1])

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
            for i in range(0, leng - 1):
                if i == leng:
                    break
                tmp1 = stack[num][i]
                tmp1_1 += stack[num][i]
                #print(f'tmp1:{tmp1}')
                tmp2 = tmp1_1 + stack[num][i + 1]
                if size < tmp2:
                    while size < tmp2:
                        size = size * 2
                    print(f'size:{size}')
                res = fib(stack[num][i])
                print(f'res:{res}')
                print(f'i:{i}')
        else:
            continue
    num += 1
    res_sum += res
print(res_sum)

# 2 10 7 1 2 5 2 9 7 32
# 1 1 1 2 1 4 1 8
#[[2, 10], [7, 1], [2, 5], [2, 9], [7, 32]]