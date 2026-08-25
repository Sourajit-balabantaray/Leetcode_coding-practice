class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        
        for i in range(1,len(nums)+2):
            if i*k not in nums:
                return i*k
            
        