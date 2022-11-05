import math
import operator
from collections import defaultdict

def solution(fees, records):

    arr = defaultdict(list)
    car = defaultdict(set)

    for x in records:
        x = x.split(" ")
        time = x[0]
        number = x[1]
        state = x[2]
        arr[number].append([time, state])
        car[number].add(0)

    for x in arr:
        if len(arr[x]) % 2 != 0:
            arr[x].append(['23:59', 'OUT'])

    for x in arr:
        time = list()
        for y in arr[x]:
            time.append(y[0])

        idx = 0
        total = 0
        for i in range(len(time) // 2):
            start = time[idx]
            end = time[idx + 1]
            total += (int(end[0:2]) * 60 + int(end[3:5])) - (int(start[0:2]) * 60 + int(start[3:5]))
            idx += 2
        if total <= fees[0]:
            car[x] = fees[1]
        else:
            car[x] = fees[1] + (math.ceil((total - fees[0]) / fees[2]) * fees[3])

    car = sorted(car.items(), key=operator.itemgetter(0))

    ans = []
    for x in car:
        ans.append(x[1])

    return ans
