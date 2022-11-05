win = [6, 6, 5, 4, 3, 2, 1]
def solution(lottos, win_nums):
    global win
    rank = 0
    for i in lottos:
        if i in win_nums:
            rank += 1

    return win[rank + lottos.count(0)], win[rank]


lottos = [45, 4, 35, 20, 3, 9]
win_nums = [20, 9, 3, 45, 4, 35]
print(solution(lottos, win_nums))