def maxsubarray(l):
    n = len(l)
    import sys
    sums = -sys.maxint
    maxs = -sys.maxint
    for i in range(n):
        if sums > 0:
            sums = l[i] + sums
        else:
            sums = l[i]
        maxs = max(maxs,sums)
    return maxs

print maxsubarray([-3,-4,-5,0,-20,20,-40])