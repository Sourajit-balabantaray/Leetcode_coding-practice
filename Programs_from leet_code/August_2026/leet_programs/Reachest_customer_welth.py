class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        l3=[]
        for i in accounts:
            l3.append(sum(i))
        return max(l3)
        