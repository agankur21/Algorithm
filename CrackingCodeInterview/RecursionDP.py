def find_magic_index_unique(list_integers, start, end):
    """
    Given an array of sorted "DISTINCT" integers find if A[i]=i for any case
    :param list_integers:
    :return:
    """
    # Since it sorted an obvious case is to use binary search. If A[i]=i then for all j < i A[j] <= j and for all
    # j > i , A[j] >= j
    if len(list_integers) ==0 or start > end or start >= len(list_integers):
        return -1
    elif start == end:
        if list_integers[start] == start:
            return start
        else:
            return -1
    else:
        mid = (start + end) / 2
        if list_integers[mid] == mid:
            return mid
        elif list_integers[mid] > mid:
            return find_magic_index_unique(list_integers, start, mid)
        else:
            return find_magic_index_unique(list_integers, mid + 1, end)

if __name__ == '__main__':
    print find_magic_index_unique([1,1,1,1,1],0,4)