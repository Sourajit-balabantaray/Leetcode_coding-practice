class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        seen={}
        for i in nums:
            if i in seen:
                seen[i]+=1
            else:
                seen[i]=1
        mid=(len(nums)//2)
        if seen[nums[mid]]>1:
            return False
        return True

        