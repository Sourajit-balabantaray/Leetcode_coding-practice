class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen={}
        for i in s:
            if i in seen:
                seen[i]+=1
            else:
                seen[i]=1
        
        for j,k in seen.items():
            if k==1:
                f=s.index(j)
        if f==0:
            return -1
        else:
            return f
        