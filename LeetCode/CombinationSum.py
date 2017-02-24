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


    def backtrack_combination(self,candidates,target,start,out_list,temp_list,used):
            if target == 0:
                out_list.append(list(temp_list))
            else:
                for i in range(start,len(candidates)):
                    candidate = candidates[i]
                    if target < candidate:
                        break
                    else:
                        if i > 0 and (candidates[i] != candidates[i-1] or used[i-1]):
                            temp_list.append(candidate)
                            used[i]=True
                            self.backtrack_combination(candidates,target-candidate,i+1,out_list,temp_list,used)
                            temp_list.pop()
                            used[i]=False


    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        out_list=[]
        temp_list=[]
        used = [False]*len(candidates)
        self.backtrack_combination(candidates,target,0,out_list,temp_list,used)
        return out_list


if __name__ == '__main__':
    solution = Solution()
    print solution.combinationSum([10,1,2,7,6,1,5], 8)
    pass
