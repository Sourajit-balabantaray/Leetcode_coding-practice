class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l1=[]
        l1=s.split()
        z=len(l1[-1])
        return z        
