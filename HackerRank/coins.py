import sys


def update_out_matrix(coins, n, min_coin_value, out_matrix):
    # Base cases
    if min_coin_value == n:
        out_matrix[n][min_coin_value] = (n in coins) * 1
        return
    else:
        if min_coin_value == 0 and n == 1:
            out_matrix[1][0] = 1 * (1 in coins)
            return
        else:
            for i in range(min_coin_value, n / 2 + 1):
                out_matrix[n][min_coin_value] += out_matrix[n - i][i] * out_matrix[i][i]
            out_matrix[n][min_coin_value] += 1 * (n in coins)


def make_change(coins, n):
    out_matrix = []
    coins=sorted(coins)
    for i in range(n+1):
        out_matrix.append([0] * (n+1))
    for i in range(1, n + 1):
        for j in range(1, i+1):
            update_out_matrix(coins, i, j, out_matrix)
    return out_matrix[n][1]


n, m = raw_input().strip().split(' ')
n, m = [int(n), int(m)]
coins = map(int, raw_input().strip().split(' '))
print make_change(coins, n)

