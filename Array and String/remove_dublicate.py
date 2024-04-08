'''

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]


Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4] -> [0,1,2,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

'''

def remove_dublicate(nums):
    p1 = len(nums) 
    i = 0 

    while p1 > 0 and i < p1 -1:
        if nums[i] == nums[i+1]:
            nums.pop(i)
            p1 -= 1
        else:
            i += 1
    return nums

nums = [0,0,1,1,1,2,2,3,3,4]
result = remove_dublicate(nums)
print("Nums=", result)