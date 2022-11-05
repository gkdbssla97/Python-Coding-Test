def gridlandMetro(n, m, k, track):

    rowDict = dict()

    for r, c1, c2 in track:
        print(r, c1, c2)
        rowRanges = rowDict.get(r, [])
        # print(rowRanges)
        for rRange in rowRanges:
            print(rRange)
            if c1 <= rRange[1] and c2 >= rRange[0]:
                rRange[0] = min(rRange[0], c1)
                rRange[1] = max(rRange[1], c2)
                break
        else:
            rowRanges.append([c1, c2])

        rowDict[r] = rowRanges
        print(rowDict[r])
    totalCount = n * m
    for r, rowRanges in rowDict.items():
        for c1, c2 in rowRanges:
            totalCount += c1 - c2 - 1

    return totalCount
track = [[2, 2, 3], [4, 1, 4], [4, 4, 4]]
print(gridlandMetro(4, 4, 3, track))