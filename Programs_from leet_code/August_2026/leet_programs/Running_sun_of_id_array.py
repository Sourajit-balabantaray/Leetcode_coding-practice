class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        l2=[]
        count=0
        for i in nums:
            count+=i
            l2.append(count)
        return l2
        