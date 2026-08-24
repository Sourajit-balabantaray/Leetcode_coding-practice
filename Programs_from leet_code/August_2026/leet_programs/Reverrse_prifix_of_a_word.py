class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        s=""
        l=""
        i=0
        if ch in word:
            while word[i]!=ch:
                s+=word[i]
                i+=1
            s+=word[i]
            for j in range(i+1,len(word)):
                l+=word[j]
            z=s[::-1]
            return z+l
        return word
