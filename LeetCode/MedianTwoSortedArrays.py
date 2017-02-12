class Solution(object):

    def find_nth_element(self,nums1,start1,end1,nums2,start2,end2,n):
       """
       Find the nth element in two sorted arrays
       :param nums1:
       :param start1:
       :param end1:
       :param nums2:
       :param start2:
       :param end2:
       :param n:
       :return:
       """
       mid1 = (start1 + end1)/2
       mid2 = (start2 + end2)/2
       len1 = len(nums1)
       len2 = len(nums2)
       if nums1[mid1] > nums2[mid2]:
           if n < (len1+len2 +1):
               return self.find_nth_element(nums1,start1,mid1,nums2,start2,end2,n)
           else :
               return self.find_nth_element(nums1,start1,)
       pass




    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Get middle element of nums1
        pass


if __name__ == '__main__':
    # Test Binary search
    solution = Solution()
    nums1 = [1, 2,3]
    nums2 = [1, 2]
    print solution.findMedianSortedArrays(nums1,nums2)
