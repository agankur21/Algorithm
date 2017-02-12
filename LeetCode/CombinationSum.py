class Solution(object):
    cache = {}

    def update_combination(self, candidates, min_value, balance):
        if (min_value, balance) in self.cache:
            return self.cache[(min_value, balance)]
        elif balance == 0:
            return []
        elif balance <= min_value:
            self.cache[(min_value, balance)] = None
            return None
        else:
            self.cache[(min_value, balance)] = []
            for candidate in candidates:
                if candidate <= min_value:
                    continue
                temp_balance = balance
                iterative_list = []
                while temp_balance - candidate >= 0:
                    iterative_list.append(candidate)
                    sub_list = self.update_combination(candidates, candidate, temp_balance - candidate)
                    temp_balance -= candidate
                    if sub_list is None:
                        continue
                    else:
                        if len(sub_list) == 0:
                            temp_list = iterative_list[:]
                            self.cache[(min_value, balance)].append(temp_list)
                        else:
                            for l in sub_list:
                                temp_l = l + iterative_list
                                self.cache[(min_value, balance)].append(temp_l)
            if len(self.cache[(min_value, balance)]) == 0:
                self.cache[(min_value, balance)] = None
            return self.cache[(min_value, balance)]

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        out = self.update_combination(candidates, 0, target)
        if out is None:
            return []
        else:
            return out


if __name__ == '__main__':
    solution = Solution()
    print solution.combinationSum([2,3, 5,7], 7)
    pass
