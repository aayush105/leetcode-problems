
''''
nums = [0,0,1,1,1,2,2,2,3,4] -> [0,0,1,1,2,2,3,4]
'''


def remove_dublicate1(nums):
    i = 1
    count = 1
    p1 = len(nums) 
    while p1 > 0 and i < p1:
        if nums[i] == nums[i-1]:
            count += 1
            if count > 2:
                nums.pop(i)
                p1 -= 1
            else:
                i += 1
        else:
            count = 1
            i += 1
    return nums

nums = [0,0,1,1,1,2,2,2,3,4]
print("result= ", remove_dublicate1(nums))