class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        p=s[0:k]
        q=p[::-1]
        r=s[k:]
        return q+r
        