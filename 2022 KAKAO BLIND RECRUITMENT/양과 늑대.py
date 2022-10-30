import copy
from collections import defaultdict
info = [0,0,1,1,1,0,1,0,1,0,1,1]
edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]

is_wolf = list()
num2edges = defaultdict(list)
max_sheep = 0

def solution(info, edges):
    global is_wolf, num2edges, max_sheep
    is_wolf = info

    ch = [0] * len(is_wolf)

    for main, sub in edges:
        num2edges[main].append(sub)
    # print(num2edges)

    find_max_recursive(0, ch, 0, 0, [])
    return max_sheep

def find_max_recursive(current_loc, ch, nsheep, nwolf, can_go):
    global max_sheep

    if ch[current_loc]: return
    ch[current_loc] = 1

    if is_wolf[current_loc]:
        nwolf += 1
    else:
        nsheep += 1
        max_sheep = max(max_sheep, nsheep)

    if nsheep <= nwolf: return
    can_go.extend(num2edges[current_loc])
    for next_loc in can_go:
        find_max_recursive(next_loc, copy.deepcopy(ch), nsheep,
                           nwolf, can_go=[loc for loc in can_go if not ch[loc]])

print(solution(info, edges))