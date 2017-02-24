import numpy as np
"""
Input
1    2    3
4    5    6
7    8    9

Output:
4    1    2
7    5    3
8    9    6

For 4*4 matrix
Input:
1    2    3    4
5    6    7    8
9    10   11   12
13   14   15   16

Output:
5    1    2    3
9    10   6    4
13   11   7    8
14   15   16   12
"""


def rotate_outer_layer(matrix, start_x, start_y, end_x, end_y):
    corners = (
    matrix[start_x, start_y], matrix[start_x, end_y - 1], matrix[end_x - 1, end_y - 1], matrix[end_x - 1, start_y])
    for y in range(end_y-1,start_y,-1):
        matrix[start_x,y] = matrix[start_x,y-1]
    for x in range(end_x-1,start_x+1,-1):
        matrix[x,end_y-1] = matrix[x-1,end_y-1]
    matrix[start_x+1,end_y-1] = corners[1]
    for y in range(start_y,end_y-2):
        matrix[end_x-1,y] = matrix[end_x-1,y+1]
    matrix[end_x-1,end_y-2]=corners[2]
    for x in range(start_x,end_x-2):
        matrix[x,start_y] = matrix[x+1,start_y]
    matrix[end_x-2,start_y]=corners[3]


def rotate_matrix(matrix):
    m,n=matrix.shape
    step=0
    while step< m/2 and step <= n/2:
        rotate_outer_layer(matrix,step,step,m-step,n-step)
        step +=1
    return matrix




if __name__ == '__main__':
    a = np.arange(1,17).reshape(4,4)
    print a
    print  rotate_matrix(a)

