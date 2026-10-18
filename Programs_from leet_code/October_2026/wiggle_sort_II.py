from typing import List
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        l=len(nums)
        p=(l-1)//2
        q=l-1
        s=nums[:]
        for i in range(l):
            if i%2==0:
                nums[i]=s[p]
                p-=1
            else:
                nums[i]=s[q]
                q-=1