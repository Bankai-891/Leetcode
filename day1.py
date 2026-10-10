class Solution(object):
    def twoSum(self, nums, target):
        dic={}

        for i,num in enumerate(nums):
            finder = target - num

            if finder in dic:
                return [dic[finder],i]
            
            dic[num] = i

sol = Solution()       
nums = [1,4,6,9,11,14]
target =10
print(sol.twoSum(nums,target))