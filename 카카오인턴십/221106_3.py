import math

def solution(box):
    idx = 0
    # Write your code here
    if box[0] == max(box):
        return box[0]
    else:
        max_val = max(box)
        min_val = min(box)

        for i in range(len(box)):
            if max_val == box[i]:
                idx = i
        # box = box[0: idx + 1]
        print(box)
        res = -1
        while box.count(max(box)) == 1:
            max_val = max(box)
            min_val = min(box)
            print(max_val, min_val)
            res = (max_val + min_val) // 2

            box[box.index(max_val)] = res
            box[box.index(min_val)] = res
            print(box)
        return res


box = [5, 15, 19]
print(solution(box))