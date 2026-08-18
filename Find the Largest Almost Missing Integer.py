class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        subarr = []
        
        for i in range(len(nums) - k + 1):
            arr = []
            
            for j in range(i, i + k):
                arr.append(nums[j])
            
            subarr.append(arr)

            ans=-1

            for l in nums:
                count=0

                for arr in subarr:
                    if l in arr:
                        count+=1
                if count==1:
                    ans=max(ans,l)

        return ans
            


        
