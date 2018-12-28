
def count_inversions(inlist):
    inversions = 0
    for i in range(len(inlist)):
        for j in range(i, len(inlist)):
            if inlist[i] <= inlist[j]:
                pass
            else:
                inversions += 1
    return inversions
