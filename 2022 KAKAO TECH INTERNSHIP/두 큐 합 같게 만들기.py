import copy
from collections import deque

# queue1 = [3, 2, 7, 2]
# queue2 = [4, 6, 5, 1]

queue1 = [1, 1]
queue2 = [1, 5]

queue1 = deque(queue1)
queue2 = deque(queue2)
length = len(queue1)

res = 0
flag = 0
sum1 = sum(queue1)
sum2 = sum(queue2)
for _ in range(length * 4):
    if sum1 > sum2:
        queue2.append(queue1.popleft())
        sum1 -= queue2[-1]
        sum2 += queue2[-1]
    elif sum1 < sum2:
        queue1.append(queue2.popleft())
        sum1 += queue1[-1]
        sum2 -= queue1[-1]
    else:
        flag = 1
        break
    res += 1
print(res if flag == 1 else -1)
