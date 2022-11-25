def solution(sizes):

    max_arr = []
    min_arr = []
    for w, h in sizes:
        max_arr.append(max(w, h))
        min_arr.append(min(w, h))
    return max(max_arr) * max(min_arr)


print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]	))