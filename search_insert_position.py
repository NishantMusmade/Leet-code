# Given a sorted array of distinct integers and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

def binarySearch(nums,target):
    low = 0 
    high = len(nums) -1

    while low<=high:
        mid = (low+high)//2
        if target < nums[mid]:
            high = mid-1
        elif target > nums[mid]:
            low = mid + 1
        else:
            return mid
    
    if target > nums[mid]:
        return mid+1
    else:
        print(mid)
        if mid - 1 < 0:
            return 0
        
        return mid


nums = [1,3,5,6]
target = 4

target_pos = binarySearch(nums,target)

print('Target position of given element is: ',target_pos)