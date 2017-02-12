class Solution(object):
    def search_or_insert_index(self, nums, start, end, target):
        if start > end:
            return start
        elif start == end:
            if nums[start] >= target:
                return start
            else:
                return start + 1
        mid_index = (start + end) / 2
        if nums[mid_index] == target:
            return mid_index
        elif nums[mid_index] > target:
            return self.search_or_insert_index(nums, start, mid_index - 1, target)
        else:
            return self.search_or_insert_index(nums, mid_index + 1, end, target)

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.search_or_insert_index(nums, 0, len(nums) - 1, target)


if __name__ == '__main__':
    solution=Solution()
    print solution.searchInsert([1,3],0)