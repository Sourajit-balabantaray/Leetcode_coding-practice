class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        mun=nums[::-1]
        return nums+mun
        
