import random

def exchange(nums, i, j):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp


def partition(nums,start,end):
    i,j=start,end
    random_index=random.randint(start,end)
    exchange(nums, start, random_index)
    while i < j:
        while i <= end and nums[i] <= nums[start]:
            i +=1
        while j >= start and nums[j] > nums[start]:
            j -=1
        if i < j:
            exchange(nums, i, j)
    exchange(nums, j, start)
    return j

def quick_sort(nums,start,end):
    partition_index=partition(nums,start,end)
    if partition_index > start:
        quick_sort(nums,start,partition_index-1)
    if partition_index < end:
        quick_sort(nums, partition_index+1,end)


if __name__ == '__main__':
    alist = [54, 26, 93,1]
    quick_sort(alist,0,len(alist)-1)
    print(alist)