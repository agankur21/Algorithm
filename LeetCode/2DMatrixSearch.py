def get_floor(matrix, target, start, end):
    # Get base cases
    if target < matrix[start]:
        return start - 1
    elif target > matrix[end]:
        return end
    else:
        mid = (start + end) / 2
        if matrix[mid] == target:
            return mid
        elif matrix[mid] < target:
            return get_floor(matrix, target, mid + 1, end)
        else:
            return get_floor(matrix, target, start, mid)




if __name__ == '__main__':
    matrix =[1,4,6,8,20]
    print get_floor(matrix,25,0,len(matrix)-1)


