# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


def containsDuplicate(nums):
    if len(nums) == 0:
        return False
    element_count = {nums[0]:1}
    for i in nums[1:len(nums)]:
        if i not in element_count:
            element_count[i]=1
        else:
            return True
        
    return False

nums = [1,2,3,4,4]
print(containsDuplicate(nums))