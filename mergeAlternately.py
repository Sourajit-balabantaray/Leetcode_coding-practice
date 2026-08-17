class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        j=""
        k=0
        l=0
        while k<len(word1) or l<len(word2):
            if k<len(word1):
                j+=word1[k]
                k+=1
            if l<len(word2):
                j+=word2[l]
                l+=1
        return j
        
