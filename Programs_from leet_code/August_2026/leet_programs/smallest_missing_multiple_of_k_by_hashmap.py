class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        seen=set(nums)
        mult=k
        while mult in seen:
            mult+=k
        return mult
       
        
            
        