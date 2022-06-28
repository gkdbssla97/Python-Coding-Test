def digit_sum(x):
    val = []
    # while x != 0:
    #     val.append(x % 10)
    #     x //= 10
    sum = 0
    for i in str(x):
        sum += int(i)
    return sum

N = int(input())
num = list(map(int, input().split()))
max = 0
tmp = []
for x in num:
    tmp.append(digit_sum(x))

max_val = 0
for x in tmp:
    if max_val < x:
        max_val = x
for i in range(len(tmp)):
    if max_val == tmp[i]:
        print(num[i], end = ' ')
        break

'''  
max = 0 
for x in num:
    tmp = digit_sum(x)
    if max < tmp:
        max = tmp
        res = x
print(res)
'''

