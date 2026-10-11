class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        l=s1.split(" ")
        m=s2.split(" ")
        see={}
        for i in l:
            see[i]=see.get(i,0)+1
        for j in m:
           see[j]=see.get(j,0)+1
        n=[]
        for k in l:
            if see[k]==1:
                n.append(k)
        for o in m:
            if see[o]==1:
                n.append(o)
        return n

        