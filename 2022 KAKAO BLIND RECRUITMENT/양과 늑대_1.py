import copy
from collections import defaultdict

# info = [0,0,1,1,1,0,1,0,1,0,1,1]
# edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]

max_sheep = 0
isWolfOrSheep = list
tree = defaultdict(list)

def solution(info, edges):
    global max_sheep, tree, isWolfOrSheep

    isWolfOrSheep = info
    ch = [0] * len(info)

    for main, sub in edges:
        tree[main].append(sub)

    dfs(0, ch, 0, 0, [])

    return max_sheep

def dfs(cur_loc, ch, nsheep, nwolf, can_go):
    global max_sheep

    if ch[cur_loc]: return
    else:
        ch[cur_loc] = 1
        if isWolfOrSheep[cur_loc]:
            nwolf += 1
        else:
            nsheep += 1
            max_sheep = max(max_sheep, nsheep)

    if nsheep <= nwolf: return
    can_go.extend(tree[cur_loc])

    for next_loc in can_go:
        dfs(next_loc, copy.deepcopy(ch), nsheep, nwolf,
            can_go = [loc for loc in can_go if not ch[loc]])

print(solution(info, edges))

