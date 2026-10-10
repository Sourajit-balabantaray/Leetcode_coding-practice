from typing import List
class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        l=[]
        for i in nums:
            if i%2==0:
                l.append(0)
            else:
                l.append(1)
        l.sort()
        return l
        