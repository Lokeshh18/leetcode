'''1.Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

ANSWER:
'''
class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)-1):
            a=nums[i]+nums[i+1]
            if a==target:
                return [i,i+1]
sol=Solution()
nums=[2,7,11,15]
target=9
print(sol.twoSum(nums, target))
