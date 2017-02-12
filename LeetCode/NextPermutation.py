class Solution(object):
    def get_exchange_indices(self, nums):
        # Iterate from back till we find the descending step
        if len(nums) < 2:
            return -1, -1
        prev_num = nums[len(nums) - 1]
        for i in xrange(len(nums) - 2, -1, -1):
            if nums[i] < prev_num:
                replacement_index = -1
                for j in range(i + 1, len(nums)):
                    if nums[j] <= nums[i]:
                        continue
                    elif replacement_index < 0 or nums[j] <= nums[replacement_index]:
                        replacement_index = j
                return i,replacement_index
            else:
                prev_num = nums[i]

        return -1, -1


    def make_ascending(self, nums, start_index, end_index):
        # Sort the list from the start_index to end_index including
        mid_index = (end_index-start_index) / 2
        for i in range(0, mid_index + 1):
            self.exchange(nums, start_index+i, end_index - i)


    def exchange(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i, j = self.get_exchange_indices(nums)
        if i >= 0 and j >= 0:
            self.exchange(nums, i, j)
            self.make_ascending(nums, i + 1, len(nums) - 1)
        else:
            self.make_ascending(nums, 0, len(nums) - 1)


if __name__ == '__main__':
    input=[2,3,1,3,3]
    solution = Solution()
    solution.nextPermutation(input)
    print input
