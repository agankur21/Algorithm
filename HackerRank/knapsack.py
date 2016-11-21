import sys
cache={}

def  maxLength(a, k):
    key = "_".join([str(i) for i in a]) + "_val=" + str(k)
    if  key not in cache:
        if k == 0 or len(a) == 0 :
            return 0
        else:
            maxval=0
            if k>= a[-1]:
                val=max(1+ maxLength(a[0:len(a)-1],k-a[-1]),maxLength(a[0:len(a)-1],k))
            else:
                val = maxLength(a[0:len(a)-1],k)
            if val > maxval:
                maxval=val
            cache[key]= maxval
    else:
        print "Cached Value for key %s: = %d" % (key,cache[key])
    return cache[key]


if __name__ == '__main__':
    print sys.argv[1]