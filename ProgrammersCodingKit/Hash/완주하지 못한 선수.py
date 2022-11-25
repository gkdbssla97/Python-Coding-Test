from collections import defaultdict

def solution(participant, completion):
    answer = ""
    arr = defaultdict()
    for x in participant:
        if not arr.get(x):
            arr[x] = 1
        else: arr[x] += 1

    for y in completion:
        arr[y] -= 1
    for z in arr:
        if arr[z] != 0:
            answer += z
    return answer

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
print(solution(participant, completion))