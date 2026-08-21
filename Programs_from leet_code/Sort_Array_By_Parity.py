class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l1=[]
        l2=[]
        for i in nums:
            if i%2==0:
                l1.append(i)
            else:
                l2.append(i)
        l1.sort()
        l2.sort()
        l3=l1+l2
        return l3
        
