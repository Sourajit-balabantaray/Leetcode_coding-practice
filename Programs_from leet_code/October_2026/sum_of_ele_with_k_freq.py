from typing import List
class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        seen={}
        for i in nums:
            if i in seen:
                seen[i]+=1
            else:
                seen[i]=1
        add=0
        for j,l in seen.items():
            if l%k==0 :
                add+=j*l
        return add