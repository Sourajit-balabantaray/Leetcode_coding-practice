from typing import List

class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def dig(n):
            s=0
            while n>0:
                d=n%10
                s+=d
                n=n//10
            return s
        l=[]
        for i in range(len(nums)):
            if dig(nums[i])==i:
                l.append(i)
        if not l:
            return -1
        return min(l)
        