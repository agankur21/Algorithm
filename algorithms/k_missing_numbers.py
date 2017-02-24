def swap(nums1,nums2,i,j):
    temp=nums1[i]
    nums1[i]=nums2[j]
    nums2[j]=temp



def find_k_missing(nums,n,k):
    """
    Given a list of numbers from 1 to n with k missing numbers,find out the k missing numbers in O(n) time and O(k) space
    :param nums:
    :param n:
    :return:
    """
    extra_k_space=[None]*k
    for i in range(n-k):
        while(nums[i] is not None and nums[i]!=i+1):
            if nums[i] < n-k:
                swap(nums,nums,i,nums[i]-1)
            else:
                swap(nums,extra_k_space,i,nums[i]-1-len(nums))
    pass


if __name__ == '__main__':
    nums=[7,2,3,1,5]
    find_k_missing(nums,7,2)