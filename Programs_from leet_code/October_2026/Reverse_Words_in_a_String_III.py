class Solution:
    def reverseWords(self, s: str) -> str:
        l=""
        p=s.split(" ")
        for i in p:
            l+=i[::-1]
            l+=" "
        l=l[:-1]
        return l
        