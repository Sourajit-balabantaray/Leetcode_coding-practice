from typing import List
class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        seen={}
        for i in nums1:
            if i in seen:
                seen[i]+=1
            else:
                seen[i]=1
        l=[]
        for j in nums2:
            if j in seen and seen[j] > 0:
                l.append(j)
                seen[j]-=1
        return l