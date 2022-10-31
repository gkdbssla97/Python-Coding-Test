from collections import defaultdict

def solution(id_list, report, k):
    arr = defaultdict(set)
    reportMan = defaultdict(set)
    id_list1 = defaultdict(list)

    for x in report:
        x = x.split(" ")
        arr[x[1]].add(x[0])
        reportMan[x[0]].add(x[1])

    for x in id_list:
        id_list1[x].append(0)

    # print(arr)
    # print(reportMan)
    for a, b in arr.items():
        if len(b) >= k:
            for x, y in reportMan.items():
                if a in y:
                    id_list1[x].append(1)

    # print(id_list1)
    answer = []
    for x, y in id_list1.items():
        answer.append(y.count(1))

    return answer

