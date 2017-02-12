class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        elements_considered = set([])
        solution_set = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            elif nums[i] in elements_considered:
                continue
            else:
                elements_considered.add(nums[i])
            left_flag = i + 1
            right_flag = len(nums) - 1
            previous_left_value = None
            previous_right_value = None
            while left_flag < right_flag:
                if previous_left_value is not None and nums[left_flag] == previous_left_value:
                    left_flag += 1
                    continue
                elif previous_right_value is not None and nums[right_flag] == previous_right_value:
                    right_flag -= 1
                    continue
                else:
                    if nums[left_flag] + nums[right_flag] + nums[i] == 0:
                        solution_set.append([nums[i], nums[left_flag], nums[right_flag]])
                        previous_left_value = nums[left_flag]
                        previous_right_value = nums[right_flag]
                        left_flag += 1
                        right_flag -= 1
                    elif nums[left_flag] + nums[right_flag] + nums[i] > 0:
                        right_flag -= 1
                    else:
                        left_flag += 1
        return solution_set


if __name__ == '__main__':
    solution = Solution()
    print solution.threeSum([-4, -2, 1, -5, -4, -4, 4, -2, 0, 4, 0, -2, 3, 1, -5, 0])
