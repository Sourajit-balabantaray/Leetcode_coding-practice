class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i,s in enumerate(nums):
            diff=target-s

            if diff in seen:
                return (seen[diff],i)

            seen[s]=i
        
