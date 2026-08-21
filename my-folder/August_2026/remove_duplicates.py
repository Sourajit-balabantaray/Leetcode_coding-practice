class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen=set()
        result=[]
        for i in nums:
            if i not in seen:
                result.append(i)
            seen.add(i)
        k=len(result)
        nums[:len(result)]=result
        nums[len(result):]=['_']*(len(nums)-len(result))
        return k
        
