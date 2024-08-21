nums = [2,7,11,15]
target = 9
flag = 0
indices = []

for i in nums:
    j = i
    for j in nums:
        if j != i:
            sum= j+i
            if sum == target:
                flag = 1
                indices.append(i)
                indices.append(j)
                break
    break
        
print(indices)  


# class Solution(object):
#     def twoSum(self, nums, target):
#         indices = []
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     indices.append(i)
#                     indices.append(j)
#                     return indices
#         return indices  # in case no solution is found

# # Test the solution
# nums = [2, 7, 11, 15]
# target = 9
# ret = Solution().twoSum(nums, target)
# print(ret)
