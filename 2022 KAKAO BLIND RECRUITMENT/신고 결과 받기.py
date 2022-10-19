from collections import defaultdict
id_list = ["muzi", "frodo", "apeach", "neo"]
#id_list = ["con", "ryan"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

#report = ["ryan con", "ryan con", "ryan con", "ryan con"]
def solution(id_list, report, k):
    answer = [0] * len(id_list)
    dic_report = {id: [] for id in id_list}
    for i in set(report):
        i = i.split()
        dic_report[i[1]].append(i[0])
    print(dic_report)
    for key, value in dic_report.items():
        if len(value) >= k:
            for j in value:
                answer[id_list.index(j)] += 1
    return answer
print(solution(id_list, report, k))

# report = list(set(report))
# board = defaultdict(list)
# time = defaultdict(list)
#
# for x in report:
#     x = x.split()
#     board[x[0]].append(x[1])
#     time[x[1]].append(1)
#
# res = defaultdict(list)
# for x in board.items():
#     for i in x[1]:
#         if len(time.get(i)) >= k:
#             res[x[0]].append(1)
#
# result = []
# print(id_list)
# for x in id_list:
#     if res.get(x) == None:
#         result.append(0)
#     else: result.append(len(res.get(x)))
#
# print(result)
