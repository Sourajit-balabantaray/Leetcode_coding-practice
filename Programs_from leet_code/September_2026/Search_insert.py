class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
           i = 0
           while i < len(nums) and nums[i] < target:
                i += 1

        return i
        