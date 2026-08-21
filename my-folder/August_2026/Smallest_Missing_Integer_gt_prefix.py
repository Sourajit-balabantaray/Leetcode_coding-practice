class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        l2=[nums[0]]
        for i in range(len(nums)-1):
            if nums[i+1]==nums[i]+1:
                l2.append(nums[i+1])
            else:
                break
        count=0
        for j in l2:
            count=count+j
        while count in nums:
            count += 1

        return count
