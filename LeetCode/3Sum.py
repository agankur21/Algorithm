# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
#
# Note: The solution set must not contain duplicate triplets.
#
# For example, given array S = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

class Solution(object):
    def get_positive_negative_zero_set(self,nums):
        positive_list=[]
        negative_list=[]
        zero_list=[]
        for i in nums:
            if i ==0:
                zero_list.append(i)
            elif i > 0:
                positive_list.append(i)
            else:
                negative_list.append(i)
        return positive_list,negative_list,zero_list

    def intersection(self,negative_list,positive_list):
        negative_flag=0
        positive_flag=0
        out=[]
        prev_negative_element=None
        prev_positive_element = None
        while negative_flag < len(negative_list) and positive_flag < len(positive_list):
            if prev_negative_element is not None and negative_list[negative_flag] == prev_negative_element:
                negative_flag +=1
                continue
            elif prev_positive_element is not None and positive_list[positive_flag] == prev_positive_element:
                positive_flag +=1
                continue
            if -1*negative_list[negative_flag] == positive_list[positive_flag]:
                out.append([0,negative_list[negative_flag],positive_list[positive_flag]])
                prev_positive_element= positive_list[positive_flag]
                prev_negative_element = negative_list[negative_flag]
                negative_flag +=1
                positive_flag+=1
            elif -1*negative_list[negative_flag] < positive_list[positive_flag]:
                negative_flag +=1
            else:
                positive_flag +=1
        return  out


    def find_elements_with_sum(self, list_elements, abs_sum, sign_identifier):
        right_flag=len(list_elements)-1
        left_flag = 0
        out=[]
        if len(list_elements) ==0 or abs_sum <= list_elements[0]:
            return out
        prev_left_element = None
        prev_right_element = None
        while left_flag< right_flag:
            if prev_left_element is not None and list_elements[left_flag] == prev_left_element:
                left_flag +=1
                continue
            if prev_right_element is not None and list_elements[right_flag] == prev_right_element:
                right_flag -=1
                continue
            current_sum = abs(list_elements[left_flag]+list_elements[right_flag])
            if current_sum == abs_sum:
                out.append([list_elements[left_flag], list_elements[right_flag], abs_sum*sign_identifier])
                prev_left_element = list_elements[left_flag]
                prev_right_element = list_elements[right_flag]
                left_flag += 1
                right_flag -=1
            elif current_sum < abs_sum:
                left_flag +=1
            else:
                right_flag -=1
        return out

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        solution_set=[]
        positive_list, negative_list, zero_list = self.get_positive_negative_zero_set(nums)
        positive_list.sort()
        negative_list.sort(reverse=True)
        if len(zero_list) > 2:
            solution_set.append([0,0,0])
        if len(zero_list) >=1:
            solution_set += self.intersection(negative_list,positive_list)

        #For each element in positive list find 2 elements in negative list , such that sum =0
        prev_element=None
        for element in positive_list:
            if prev_element is  not None and element == prev_element:
                continue
            else:
                solution_set += self.find_elements_with_sum(negative_list,element,1)
                prev_element=element
        #For each element in negative list find 2 elements in positive list , such that sum =0
        prev_element = None
        for element in negative_list:
            if prev_element is  not None and element == prev_element:
                continue
            else:
                solution_set += self.find_elements_with_sum(positive_list,-1*element,-1)
                prev_element = element
        return solution_set


if __name__ == '__main__':
    solution  =Solution()
    print solution.threeSum([-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0])
