class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        seen={val}
        result=[]
        for i in nums:
            if i not in seen:
                result.append(i)
        k=len(result)

        nums[:len(result)]=result
        nums[len(result):]=['_']*(len(nums)-len(result))
        return k
        
