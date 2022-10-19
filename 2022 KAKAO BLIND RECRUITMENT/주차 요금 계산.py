import math
from collections import defaultdict

fees = [120, 0, 60, 591]
records = ["16:00 3961 IN", "16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]

arr = defaultdict(list)

for record in records:
    record = record.split()
    arr[record[1]].append((record[0], record[2]))

for x in arr:
    if len(arr[x]) % 2 != 0:
        arr[x].append(("23:59", 'OUT'))
print(arr)
result = []
for x in arr:
    idx = 0
    res = 0
    while idx < len(arr[x]):
        time1 = arr[x][idx][0]
        time1 = time1.split(":")

        time2 = arr[x][idx + 1][0]
        time2 = time2.split(":")
        res += ((60 * int(time2[0])) + int(time2[1])) - ((60 * int(time1[0])) + int(time1[1]))
        idx += 2
    if res <= fees[0]:
        result.append([x, fees[1]])
    else:
        print(res if x == '0000' else 0)
        total = fees[1] + math.ceil((res - fees[0]) / fees[2]) * fees[3]
        result.append([x, total])
result.sort()
answer = []
for x in result:
    answer.append(x[1])
print(answer)