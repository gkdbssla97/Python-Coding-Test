def solution(answers):
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ]

    first = first * (10000 // len(first))
    second = second * (10000 // len(second))
    third = third * (10000 // len(third))

    score = dict()
    score[1] = 0
    score[2] = 0
    score[3] = 0
    idx = 0
    for x, y, z in zip(first, second, third):
        if x == answers[idx]:
            score[1] += 1
        if y == answers[idx]:
            score[2] += 1
        if z == answers[idx]:
            score[3] += 1
        idx += 1
        if idx == len(answers):
            break

    answer = []
    for x in score.items():
        if max(score.values()) == x[1]:
            answer.append(x[0])
    return answer
