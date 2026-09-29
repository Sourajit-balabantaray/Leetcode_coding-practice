class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
        seen = {}

        for i in nums:
            if i % 2 == 0:
                if i in seen:
                    seen[i] += 1
                else:
                    seen[i] = 1

        maxi = 0
        ans = -1

        for j in seen:
            if seen[j] > maxi:
                maxi = seen[j]
                ans = j
            elif seen[j] == maxi and j < ans:
                ans = j

        return ans