class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0 or len(nums) == 1:
            return 0
        else:
            current_index = 0
            max_index = nums[0]
            jumps = 0
            while max_index < len(nums) - 1:
                jumps += 1
                level_max = max_index
                for current_index in range(current_index, level_max+1):
                    max_index = max(max_index, current_index + nums[current_index])
                current_index +=1
            return jumps + 1

if __name__ == '__main__':
    solution = Solution()
    nums = [1,2,3]
    print solution.jump(nums)
