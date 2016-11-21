def array_left_rotation(a, n, k):
    back_array = a[0:k]
    return a[k:n] + back_array


n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k);
print ' '.join(map(str, answer))