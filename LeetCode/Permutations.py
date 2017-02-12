class Solution:
    def backtrack_duplicates(self, nums, out_list, temp_list, used):
        if len(temp_list) == len(nums):
            out_list.append(list(temp_list))
        else:
            for i in range(len(nums)):
                if used[i] == True or (i > 0 and nums[i] == nums[i - 1] and used[i - 1] == False):
                    continue
                used[i] = True
                temp_list.append(nums[i])
                self.backtrack_duplicates(nums, out_list, temp_list, used)
                used[i] = False
                temp_list.pop()

    def backtrack_unique(self, nums, out_list, temp_list):
        if len(temp_list) == len(nums):
            out_list.append(list(temp_list))
        else:
            for num in nums:
                if num in temp_list:
                    continue
                else:
                    temp_list.append(num)
                    self.backtrack_unique(nums, out_list, temp_list)
                    temp_list.pop()

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        out_list = []
        temp_list = []
        used = [False]*len(nums)
        nums.sort()
        self.backtrack_duplicates(nums, out_list, temp_list)
        return out_list


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 1, 2]
    print solution.permute(nums)
