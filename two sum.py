class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)-1):
            for j in range (1,(len(nums))):
                a=nums[i]+nums[j]
                if a==target:
                    if i != j:
                        return [i,j]
sol=Solution()
nums=[2,7,11,15]
target=9
print(sol.twoSum(nums, target))
