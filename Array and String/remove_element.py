'''
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
'''

def remove_element(nums, val):
    p1 = len(nums)
    i = 0
    while i < p1:
        if nums[i] == val:
            nums.remove(val)
            p1 -= 1
        else:
            i += 1
    return len(nums), nums

num = [0,1,2,2,3,0,4,2]
val = 2
length , result = remove_element(num, val)
print(length, "nums =", result)
