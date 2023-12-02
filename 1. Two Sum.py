class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            complement = target - nums[i]
            for j, item in enumerate(nums):
                if item == complement and i != j:
                    return [i, j]
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i != j and abs(nums[i]):
        #             if nums[i] + nums[j] == target:
        #                 return [i, j]


nums = [-3, 4, 3, 90]
target = 0
s = Solution()
print(s.twoSum(nums, target))
