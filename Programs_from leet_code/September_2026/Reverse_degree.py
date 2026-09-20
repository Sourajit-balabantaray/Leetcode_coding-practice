class Solution:
    def reverseDegree(self, s: str) -> int:
        Sum=0
        for i,j in enumerate(s,1):
            x=ord(j)-ord('a')
            Sum+=(26-x)*(i)
        return Sum
        