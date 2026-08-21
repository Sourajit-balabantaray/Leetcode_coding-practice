class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        l1=[]
        l2=[]
        l3=[]
        for i in nums:
            if i%2==0:
                l1.append(i)
            else:
                l2.append(i)
        j=0
        k=0
        l=0
        while(k!=len(nums)):
            if k%2==0:
                l3.append(l1[j])
                j+=1
            else:
                l3.append(l2[l])
                l+=1
            k+=1
        return l3
        
