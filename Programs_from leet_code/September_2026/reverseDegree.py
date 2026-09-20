class Solution:
    def reverseDegree(self, s: str) -> int:
        Sum=0
        for i in range(len(s)):
            x=ord(s[i])-ord('a')
            Sum+=(26-x)*(i+1)
        return Sum
        