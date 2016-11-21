def print_string_permutations(balance_string,length_string):
    if length_string == 0:
        print balance_string
    else:
        for i in range(1, 4):
            print_string_permutations(balance_string+str(i),length_string-1)


def recurse_string(n):
    print_string_permutations("",n)


if __name__ == '__main__':
    recurse_string(3)


