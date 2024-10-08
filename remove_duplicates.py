# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
# The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. 
# The remaining elements of nums are not important as well as the size of nums.
# Return k.

def removeDuplicates(nums):
    i = 0  #to maintain index of unique elements
    for x in range(1,len(nums)):
        if nums[x] != nums[i]:
            i+=1
            nums[i] = nums[x]
        
    return i + 1

nums = [0,0,0,1,1,1,2,3,4,4,4,5,6,7,7,7]
k = removeDuplicates(nums)

print('Number of unique elements: ',k)
print('List of unique elements: ',nums[:k])
