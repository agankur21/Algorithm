class Solution:
    def subsets(self, nums):
        nums.sort()
        out_list = []
        temp_list = []
        self.backtrack_duplicates(out_list, temp_list, nums, 0)
        return out_list

    def backtrack_unique(self, out_list, temp_list, nums, start):
        out_list.append(list(temp_list))
        for i in range(start, len(nums)):
            temp_list.append(nums[i])
            self.backtrack_unique(out_list, temp_list, nums, i + 1)
            temp_list.pop()

    def backtrack_duplicates(self, out_list, temp_list, nums, start):
        out_list.append(list(temp_list))
        for i in range(start, len(nums)):
            if i > start and nums[i]==nums[i-1]:
                continue
            temp_list.append(nums[i])
            self.backtrack_duplicates(out_list, temp_list, nums, i + 1)
            temp_list.pop()

if __name__ == '__main__':
    solution = Solution()
    print solution.subsets([1,2,2])