def hackerlandRadioTransmitters(x, k):
    x.sort()
    nAntCnt = 0

    nPos = 0
    nBefore = 0
    nAfter = 1
    nXlen = len(x)

    if nXlen == 1:
        return 1
    print(x)
    while True:
        if x[nPos] - x[nBefore] <= k:
            nPos += 1
            if nPos == nXlen:
                nAntCnt += 1
                return nAntCnt
            continue
        else:
            nAfter = nPos
            nPos -= 1

            while True:
                if x[nAfter] - x[nPos] <= k:
                    nAfter += 1
                    if nAfter == nXlen:
                        nAntCnt += 1
                        return nAntCnt
                else:
                    nAntCnt += 1
                    nBefore = nAfter
                    nPos = nAfter
                    break
    return  nAntCnt

x = [7, 2, 4, 6, 5, 9, 12, 11]
print(hackerlandRadioTransmitters(x, 2))
