class Solution:
    def targetIndices(self, nums, target):
        arr = []
        for i, number in enumerate(sorted(nums)):
            if target == number:
                arr.append(i)
        return arr


nums = [1, 2, 5, 2, 3]
target = 2
s = Solution()
print(s.targetIndices(nums, target))
