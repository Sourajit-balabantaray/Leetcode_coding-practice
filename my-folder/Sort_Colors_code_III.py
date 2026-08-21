class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count1=0
        count2=0
        count3=0
        for i in nums:
            if i==0:
                count1+=1
            elif i==1:
                count2+=1
            else:
                count3+=1
        nums[:]=[0]*count1+[1]*count2+[2]*count3
        
        
