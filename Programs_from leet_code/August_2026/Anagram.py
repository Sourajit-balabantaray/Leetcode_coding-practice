class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen={}
        if len(s)!=len(t):
            return False

        for i in s:
            if i in seen:
                seen[i]+=1
            else:
                seen[i]=1
        
        for j in t:
            if j in s:
                seen[j]-=1
            else:
                return False
        for i in seen.values():
            if i!=0:
                return False
        return True
        
