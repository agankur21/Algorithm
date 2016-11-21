def check_valid(s):
    if len(s) %2 ==0:
        return s == s[0:2]*(len(s)/2)
    else:
        return s == s[0:2]*(len(s)/2) + s[0]

s = raw_input().strip()


def get_n_choose_two(list_elements):
    out_list=[]
    for i in range(len(list_elements)):
        for j in range(i+1,len(list_elements)):
            out_list.append((list_elements[i],list_elements[j]))
    return out_list

print check_valid(s)
print get_n_choose_two(list(set(s)))
from itertools import combinations

for pair in  combinations(s,2):
    print pair