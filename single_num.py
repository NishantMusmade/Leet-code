# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

def singleNumber(nums):
    single_num = 0
    for i in nums:
        single_num ^= i

    return single_num

nums = [4,2,2,1,1]
print(singleNumber(nums))
