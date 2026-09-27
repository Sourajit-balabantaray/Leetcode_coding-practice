class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        dic={}
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        for j in nums:
            if j%2==0 and dic[j]==1:
                return j
        return -1
        