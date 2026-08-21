class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen=set()
        for i in nums:
            if i in seen:
                nums.remove(i)
            seen.add(i)
        return nums
            
